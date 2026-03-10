import os

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from typing import List
from docutils.nodes import Node
from docutils.parsers.rst import directives
from sphinx.util import logging

logger = logging.getLogger(__name__)

TYPES = ["multiple-choice","short-answer"]
VARIANTS = {"multiple-choice": ["single-select","multiple-select"], "short-answer": ["blocks"]}
FEEDBACKS = {"multiple-choice": {"single-select": {True: "Correct!", False: "Incorrect. Try again."},"multiple-select": {True: "Correct!", False: "Incorrect. Try again."}}, "short-answer": {"blocks": {True: "Correct!", False: "Incorrect. Try again."}}}
COLUMNS =  {"multiple-choice": {"single-select": "1 1 2 2", "multiple-select": "1 1 2 2"}, "short-answer": {"blocks": "not used"}}

class QuestionDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "class": directives.class_option,
        "label": directives.unchanged,
        "type": directives.unchanged,
        "variant": directives.unchanged,
        "columns": directives.unchanged,
        "admonition": directives.flag,
        "nocaption": directives.flag,
        "showanswer": directives.flag
    }

    def run(self) -> List[Node]:

        # check if the type is supported and get values:
        Type = self.options.get("type", "multiple-choice")
        if Type not in TYPES:
            message = f"Unsupported question type {Type} at line {self.lineno} in {self.env.docname}. Supported types are: {TYPES}"
            raise ValueError(message)
        Variant = self.options.get("variant", VARIANTS[Type][0])
        if Variant not in VARIANTS[Type]:
            message = f"Unsupported question variant {Variant} for type {Type} at line {self.lineno} in {self.env.docname}. Supported variants are: {VARIANTS[Type]}"
            raise ValueError(message)
        Columns = self.options.get("columns", COLUMNS[Type][Variant])
        Feedback = self.options.get("feedback", FEEDBACKS[Type][Variant])

        # see if a class and a caption has to be added to the question
        Class = self.options.get("class", [])
        Admonition = "admonition" in self.options
        NoCaption = "nocaption" in self.options
        ShowAnswer = "showanswer" in self.options

        # just create a node and store some stuff
        node = question_node()
        node["type"] = Type
        node["variant"] = Variant
        node["class"] = Class
        node["admonition"] = Admonition
        node["show_answer"] = ShowAnswer
        # create a unique id for the node, if not provided by the user:
        if self.options.get("label"):
            node_id = self.options["label"]
        else:
            # unique within the document, and hopefully globally unique
            docname = self.env.docname.replace("/", "-") # replace / with - to avoid issues with html ids
            node_id = f"question-{docname}-{self.env.new_serialno('question')}"
        node["ids"] = [node_id]
        # add the title, if needed
        title_text = ""
        if self.arguments != []:
            if NoCaption:
                title_format = "%t"
            else:
                title_format = " (%t)"
            title_text += title_format.replace("%t", self.arguments[0])
        node["nocaption"] = NoCaption
        textnodes, _ = self.state.inline_text(title_text, self.lineno)
        node_title = nodes.title(title_text, "", *textnodes,ids=[node_id + "-title"])
        node += node_title

        if Type == "multiple-choice":
            if Variant == "single-select":
                return self._handle_multiple_choice_single_select(node, node_id, Columns, Feedback)
            elif Variant == "multiple-select":
                return self._handle_multiple_choice_multiple_select(node, node_id, Columns, Feedback)
        elif Type == "short-answer":
            if Variant == "blocks":
                return self._handle_short_answer_blocks(node, node_id, Feedback)
            
    def _split_input(self):
        # first get the content between --- and ---, which is the content for options.
        indexes = [i for i, val in enumerate(self.content) if val.strip() == "---"]
        if len(indexes) == 0:
            message = f"No options provided for question at line {self.lineno} in {self.env.docname}. Please provide options between --- and ---."
            raise ValueError(message)
        elif len(indexes) == 1:
            message = f"Only one --- found for question at line {self.lineno} in {self.env.docname}. Please provide options between --- and ---."
            raise ValueError(message)
        elif len(indexes) > 2:
            message = f"More than two --- found for question at line {self.lineno} in {self.env.docname}. Please provide options between --- and ---. Extra --- found at lines: {', '.join([str(self.lineno + i) for i in indexes[2:]])}"
            raise ValueError(message)
        
        # split in pre-text, options and post-text:
        options_raw = self.content[indexes[0]+1:indexes[1]]
        pre_text = self.content[:indexes[0]]
        post_text = self.content[indexes[1]+1:]

        return pre_text, options_raw, post_text

    def _handle_short_answer_blocks(self, node, node_id, Feedback):

        # split the content into pre-text, options and post-text
        pre_text, options_raw, post_text = self._split_input()

        # add the first text if any
        if pre_text:
            pre_section = nodes.section(classes=[f"question-pretext"],ids=[node_id + "-pretext"])
            self.state.nested_parse(pre_text, self.content_offset, pre_section)
            node += pre_section

        # parse the options (just include currently)
        
        type_list = []
        answer_list = []
        label_list = []
        correct_list = []
        incorrect_list = []
        if options_raw:
            # find all the options, which start with a line that starts with "T[", "TI[", "TF[" (possible with leading spaces)
            indexes = [i for i, val in enumerate(options_raw) if val.strip()[1:].startswith("[") or val.strip()[2:].startswith("[")]
            for i in range(len(indexes)):
                block = options_raw[indexes[i]:indexes[i+1]] if i < len(indexes)-1 else options_raw[indexes[i]:]
                
                # get the type of the question from the first line, which should start with "T[", "TI[", "TF["
                type_list.append(block[0].strip().split("[")[0].strip())

                # get correct answer from first line
                answer = block[0].strip().split("[")[1].strip()
                answer = answer.split(']')[0].strip()
                answer_list.append(answer)

                # Get the label from the first line if it exists (after the answer and between parentheses)
                label = block[0].strip()[2:]
                label = [label.split(']')[1].strip()]
                line = 1
                while line < len(block):
                    if block[line].strip().startswith("> ") or block[line].strip().startswith("= "):
                        break
                    label.append(block[line].strip())
                    line += 1
                label_list.append(label)

                # get feedback from lines starting with > (incorrect) or = (correct)
                correct_feedback = []
                incorrect_feedback = []
                if line < len(block):
                    while line < len(block):
                        if block[line].strip().startswith("> "):
                            if len(incorrect_feedback) > 0:
                                incorrect_feedback.append("") # add an empty line between different feedback blocks for better readability
                            incorrect_feedback.append(block[line].strip()[2:])
                            last = "incorrect"
                        elif block[line].strip().startswith("= "):
                            if len(correct_feedback) > 0:
                                correct_feedback.append("") # add an empty line between different feedback blocks for better readability
                            correct_feedback.append(block[line].strip()[2:])
                            last = "correct"
                        else:
                            if last == "incorrect":
                                incorrect_feedback.append(block[line].strip())
                            else:
                                correct_feedback.append(block[line].strip())
                        line += 1
                else: # this means that no feedback is provided after an optional label, so we use default feedback based on correct/incorrect status
                    correct_feedback = [Feedback[True]]
                    incorrect_feedback = [Feedback[False]]
                correct_list.append(correct_feedback)
                incorrect_list.append(incorrect_feedback)

        # Create the lines that will render a full-width card with
        # - the label in the header
        # - the input field in the body
        # - the feedback in the footer
        options_content = []
        for label in label_list:
            card = [":::{card}", ":shadow: lg", ":width: 100%",":class-card: option",":class-body: input"]
            if label == ['']:
                card.append(":class-header: hidden")
            card.extend(["^^^","+++",":::"])
            options_content.extend(card)

        # add the options section
        options_section = nodes.section(classes=[f"question-options"],ids=[node_id + "-options"])
        self.state.nested_parse(options_content, self.content_offset, options_section)
        node += options_section

        # loop over the cards in the section, and add the label, input field and feedback to the correct place in the card:
        current_card = -1
        for nd in options_section.findall():
            if isinstance(nd,nodes.container):
                if "sd-card-header" in nd.get("classes", []):
                    current_card += 1
                    # add the label to the header:
                    label_content = label_list[current_card]
                    label_content_section = nodes.section(classes=["question-option-label"],ids=[f"{node_id}-option-{current_card}-label"])
                    self.state.nested_parse(label_content, self.content_offset, label_content_section)
                    nd += label_content_section
                if "sd-card-body" in nd.get("classes", []):
                    # add the input field to the body, based on the type of the answer:
                    if type_list[current_card] in ["T", "TI", "TF"]:
                        raw_html = f"<textarea class='question-option-input type-{type_list[current_card]}' id='{node_id}-option-{current_card}-input' placeholder='Insert your answer here...'></textarea>"
                    # elif type_list[current_card] == "M":
                        # raw_html = f"<input type='number' class='question-option-input' id='{node_id}-option-{current_card}-input' placeholder='Insert your answer here...'>"
                    else: 
                        message = f"Unsupported question type {type_list[current_card]} for short answer question at line {self.lineno + indexes[current_card] + 1} in {self.env.docname}. Supported types are: T, N and M."
                        raise ValueError(message)
                    input_field = nodes.raw(raw_html, raw_html, format="html")
                    nd += input_field
                    # add a section with the correct answer with plain content (not parsed, to avoid issues with parsing math or other content in the correct answer)
                    answer_content = answer_list[current_card]
                    answer_content_section = nodes.section(classes=["question-option-answer"],ids=[f"{node_id}-option-{current_card}-answer"])
                    answer_content_section += nodes.paragraph(text=answer_content)
                    nd += answer_content_section
                if "sd-card-footer" in nd.get("classes", []):
                    # add the content of the correct feedback to the footer:
                    correct_feedback_content = correct_list[current_card]
                    correct_feedback_content_section = nodes.section(classes=["question-feedback correct"],ids=[f"{node_id}-option-{current_card}-feedback"])
                    self.state.nested_parse(correct_feedback_content, self.content_offset, correct_feedback_content_section)
                    nd += correct_feedback_content_section
                    incorrect_feedback_content = incorrect_list[current_card]
                    incorrect_feedback_content_section = nodes.section(classes=["question-feedback incorrect"],ids=[f"{node_id}-option-{current_card}-feedback-incorrect"])
                    self.state.nested_parse(incorrect_feedback_content, self.content_offset, incorrect_feedback_content_section)
                    nd += incorrect_feedback_content_section

        # include the final text, if any
        if post_text:
            post_section = nodes.section(classes=[f"question-posttext"],ids=[node_id + "-posttext"])
            self.state.nested_parse(post_text, self.content_offset, post_section)
            node += post_section

        # include a button inside a section to reset the question and to submit the question
        button_section = nodes.section(classes=[f"question-buttons"],ids=[node_id + "-buttons"])
        # calculate number of buttons (at most)
        buttonCount = 2 # always the submit and reset button
        if node["show_answer"]:
            buttonCount += 1 # if show answer button is needed
        # create four values, where the lowest is 1, the highest is buttonCount
        # and the two middle values are linear interpolated between 1 and buttonCount
        # and afterward rounded to the nearest integer
        buttonDist = [1]
        if buttonCount > 1:
            buttonDist.append(round(1 + (buttonCount - 1) / 3))
            buttonDist.append(round(1 + 2 * (buttonCount - 1) / 3))
            buttonDist.append(buttonCount)
        else:
            buttonDist.extend([1,1,1])
        # convert to string
        buttonDist = " ".join([str(x) for x in buttonDist])
        grid = [f"::::{{grid}} {buttonDist}",":gutter: 3",""]
        left_button = [":::{grid-item-card}", ":shadow: lg",":text-align: center", ":class-card: submit-button","","Submit answer(s)",":::"]
        grid.extend(left_button)
        if node["show_answer"]:
            middle_button = [":::{grid-item-card}", ":shadow: lg",":text-align: center", ":class-card: show-button","","Show answer(s)",":::"]
            grid.extend(middle_button)
        right_button = [":::{grid-item-card}", ":shadow: lg",":text-align: center", ":class-card: reset-button","", "Try again",":::"]
        grid.extend(right_button)
        grid.extend(["::::"])
        self.state.nested_parse(grid, self.content_offset, button_section)
        node += button_section

        return [node]
            
    def _handle_multiple_choice_shared(self, node, node_id, Columns, Feedback):
        # split the content into pre-text, options and post-text
        pre_text, options_raw, post_text = self._split_input()

        mc_list = []
        fb_list = []
        ci_list = []
        if options_raw:
            # find all the options, which start with a line that starts with "[ ] " or "[x] " (possible with leading spaces)
            indexes = [i for i, val in enumerate(options_raw) if val.strip().startswith("[ ] ") or val.strip().startswith("[x] ")]
            for i in range(len(indexes)):
                raw_option = options_raw[indexes[i]:indexes[i+1]] if i < len(indexes)-1 else options_raw[indexes[i]:]
                fb_index = [f for f, val in enumerate(raw_option) if val.strip().startswith("> ")]
                ci_list.append(raw_option[0].strip()[1] == "x") # correct if it starts with [x]
                if fb_index:
                    mc_content = raw_option[:fb_index[0]]
                    mc_content[0] = mc_content[0].strip()[3:] # remove the [ ] or [x] and leading spaces
                    fb_content = raw_option[fb_index[0]:]
                    fb_content[0] = fb_content[0].strip()[2:] # remove the "> " and leading spaces
                else:
                    mc_content = raw_option
                    mc_content[0] = mc_content[0].strip()[3:] # remove the [ ] or [x] and leading spaces
                    fb_content = [Feedback[ci_list[-1]]] # use default feedback based on correct/incorrect status
                mc_list.append(mc_content)
                fb_list.append(fb_content)
        
        # check the number of correct answers
        if sum(ci_list)==0 and node["variant"]=="single-select":
            message = f"No correct options provided for multiple-choice single-select question at line {self.lineno} in {self.env.docname}. Please provide at least one correct option between --- and ---."
            raise ValueError(message)
                
        # Start the grid for the cards:
        cards = [f"::::{{grid}} {Columns}",":gutter: 3",""]
        # create empty cards for each of the options
        for mc in mc_list:
            cards.append(":::{grid-item-card}")
            cards.append(":shadow: lg")
            cards.append(":class-card: option")
            cards.append("+++")
            cards.append(":::")   
        # end the grid
        cards.append("::::")

        # add the first text if any
        if pre_text:
            pre_section = nodes.section(classes=[f"question-pretext"],ids=[node_id + "-pretext"])
            self.state.nested_parse(pre_text, self.content_offset, pre_section)
            node += pre_section
        
        # add the mc options section (should be given)
        mc_section = nodes.section(classes=[f"question-options"],ids=[node_id + "-options"])
        self.state.nested_parse(cards, self.content_offset, mc_section)
        node += mc_section
        # loop over the options and add the content of the option (parsed) to the card:
        current_card = -1
        for nd in mc_section.findall():
            if isinstance(nd,nodes.container):
                if "sd-card-body" in nd.get("classes", []):
                    current_card += 1
                    # add the content of the option to the card:
                    option_content = mc_list[current_card]
                    option_content_section = nodes.section(classes=["question-option"],ids=[f"{node_id}-option-{current_card}"])
                    self.state.nested_parse(option_content, self.content_offset, option_content_section)
                    nd += option_content_section
                if "sd-card-footer" in nd.get("classes", []):
                    # add the content of the feedback to the card:
                    feedback_content = fb_list[current_card]
                    feedback_content_section = nodes.section(classes=[f"question-feedback {'' if ci_list[current_card] else 'in'}correct"],ids=[f"{node_id}-feedback-{current_card}"])
                    self.state.nested_parse(feedback_content, self.content_offset, feedback_content_section)
                    feedback_content_section["data-correct"] = ci_list[current_card] # add data attribute for correct/incorrect status, which can be used by the frontend to show feedback
                    nd += feedback_content_section

        # include the final text, if any
        if post_text:
            post_section = nodes.section(classes=[f"question-posttext"],ids=[node_id + "-posttext"])
            self.state.nested_parse(post_text, self.content_offset, post_section)
            node += post_section

        return node

    def _handle_multiple_choice_single_select(self, node, node_id, Columns, Feedback):
        
        node = self._handle_multiple_choice_shared(node, node_id, Columns, Feedback)

        # include a button inside a section to reset the question
        button_section = nodes.section(classes=[f"question-buttons"],ids=[node_id + "-buttons"])
        # calculate number of buttons (at most)
        buttonCount = 1 # always the reset button
        if node["show_answer"]:
            buttonCount += 1 # if show answer button is needed
        # create four values, where the lowest is 1, the highest is buttonCount
        # and the two middle values are linear interpolated between 1 and buttonCount
        # and afterward rounded to the nearest integer
        buttonDist = [1]
        if buttonCount > 1:
            buttonDist.append(round(1 + (buttonCount - 1) / 3))
            buttonDist.append(round(1 + 2 * (buttonCount - 1) / 3))
            buttonDist.append(buttonCount)
        else:
            buttonDist.extend([1,1,1])
        # convert to string
        buttonDist = " ".join([str(x) for x in buttonDist])
        grid = [f"::::{{grid}} {buttonDist}",":gutter: 3",""]
        # Only add the show button if requested
        if node["show_answer"]:
            left_button = [":::{grid-item-card}", ":shadow: lg",":text-align: center", ":class-card: show-button","","Show answer(s)",":::"]
            grid.extend(left_button)
        # Always add the reset button
        right_button = [":::{grid-item-card}", ":shadow: lg",":text-align: center", ":class-card: reset-button","", "Try again",":::"]
        grid.extend(right_button)
        grid.extend(["::::"])
        self.state.nested_parse(grid, self.content_offset, button_section)
        node += button_section

        return [node]
    
    def _handle_multiple_choice_multiple_select(self, node, node_id, Columns, Feedback):
        
        node = self._handle_multiple_choice_shared(node, node_id, Columns, Feedback)

        # include a section to show feedback for the whole question (instead of per option as in single-select)
        # the content of the feedback will be determined by the frontend based on the selected options and the correct options.
        feedback_section = nodes.section(classes=[f"question-feedback overall-feedback"],ids=[node_id + "-overall-feedback"])
        grid = [f"::::{{grid}} 1",":gutter: 3",""]
        # add cards:
        # - Correct
        # - Incorrect
        correct_card = [":::{grid-item-card}", ":shadow: lg", ":class-card: correct","","Well done!",":::"]
        incorrect_card = [":::{grid-item-card}", ":shadow: lg", ":class-card: incorrect","","Try again! You selected at least one incorrect option.",":::"]
        missed_card = [":::{grid-item-card}", ":shadow: lg", ":class-card: missed","","Try again! You missed at least one correct option.",":::"]
        grid.extend(correct_card)
        grid.extend(incorrect_card)
        grid.extend(missed_card)
        grid.extend(["::::"])
        self.state.nested_parse(grid, self.content_offset, feedback_section)
        node += feedback_section

        # include a button inside a section to reset the question and to submit the question
        # (for multiple select, we need a submit button to show feedback, instead of showing
        # feedback immediately after selecting an option as in single select)
        button_section = nodes.section(classes=[f"question-buttons"],ids=[node_id + "-buttons"])
        # calculate number of buttons (at most)
        buttonCount = 2 # always the submit and reset button
        if node["show_answer"]:
            buttonCount += 1 # if show answer button is needed
        # create four values, where the lowest is 1, the highest is buttonCount
        # and the two middle values are linear interpolated between 1 and buttonCount
        # and afterward rounded to the nearest integer
        buttonDist = [1]
        if buttonCount > 1:
            buttonDist.append(round(1 + (buttonCount - 1) / 3))
            buttonDist.append(round(1 + 2 * (buttonCount - 1) / 3))
            buttonDist.append(buttonCount)
        else:
            buttonDist.extend([1,1,1])
        # convert to string
        buttonDist = " ".join([str(x) for x in buttonDist])
        grid = [f"::::{{grid}} {buttonDist}",":gutter: 3",""]
        left_button = [":::{grid-item-card}", ":shadow: lg",":text-align: center", ":class-card: submit-button","","Submit answer(s)",":::"]
        grid.extend(left_button)
        # Only add when requested
        if node["show_answer"]:
            middle_button = [":::{grid-item-card}", ":shadow: lg",":text-align: center", ":class-card: show-button","","Show answer(s)",":::"]
            grid.extend(middle_button)
        right_button = [":::{grid-item-card}", ":shadow: lg",":text-align: center", ":class-card: reset-button","", "Try again",":::"]
        grid.extend(right_button)
        grid.extend(["::::"])
        self.state.nested_parse(grid, self.content_offset, button_section)
        node += button_section

        return [node]

class question_node(nodes.Admonition, nodes.Element):
    pass

def visit_question_node(self, node: question_node) -> None:
    classes = " ".join(node["class"])
    classes += " {}".format(" ".join([node["type"], node["variant"]]))
    if node["admonition"]:
        self.body.append(self.starttag(node, "div", CLASS=f"admonition {classes}",ids=node["ids"]))
    else:
        self.body.append(self.starttag(node, "div", CLASS=f"{classes}",ids=node["ids"]))

def depart_question_node(self, node: question_node) -> None:
    if not node["nocaption"]:
        id = node.attributes.get("ids", [""])[0]
        # use the id to find the correct title location
        search_str = f'<p class="admonition-title" id="{id}-title">'
        idx = list_rindex(self.body, search_str) + 1
        element = f'<span class="caption-number">Question </span>'
        self.body.insert(idx, element)
    self.body.append("</div>")

def setup(app):
    app.add_directive("question", QuestionDirective)
    app.add_node(question_node, html=(visit_question_node, depart_question_node))
    app.add_css_file("teachbooks_questions.css")
    app.add_js_file("teachbooks_wrapadmonition.js")
    app.add_js_file("teachbooks_mcss.js")
    app.add_js_file("teachbooks_mcms.js")
    app.add_js_file("teachbooks_sab.js")
    
    static_path = os.path.join(os.path.dirname(__file__), "_static")
    app.config.html_static_path.append(static_path)
    
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

def list_rindex(li, x, skip=0) -> int:
    """Getting the last occurrence of an item in a list."""
    """Skipping the first skip occurrences from the end."""
    for i in reversed(range(len(li))):
        if li[i] == x:
            if skip == 0:
                return i
            else:
                skip -= 1
    raise ValueError("{} is not in list".format(x))