import os
from typing import List, Tuple, Dict, Any

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.nodes import Node
from docutils.parsers.rst import directives
from sphinx.util import logging

logger = logging.getLogger(__name__)


class QuestionDirective(SphinxDirective):
    # Configuration
    TYPES = ["multiple-choice", "short-answer"]
    VARIANTS = {
        "multiple-choice": ["single-select", "multiple-select"],
        "short-answer": ["blocks"],
    }
    FEEDBACKS = {
        "multiple-choice": {
            "single-select": {True: "Correct!", False: "Incorrect. Try again."},
            "multiple-select": {True: "Correct!", False: "Incorrect. Try again."},
        },
        "short-answer": {"blocks": {True: "Correct!", False: "Incorrect. Try again."}},
    }
    COLUMNS = {
        "multiple-choice": {"single-select": "1 1 2 2", "multiple-select": "1 1 2 2"},
        "short-answer": {"blocks": "not used"},
    }
    
    # Patterns
    OPTION_CHECKBOX_UNCHECKED = "[ ] "
    OPTION_CHECKBOX_CHECKED = "[x] "
    FEEDBACK_WRONG_PREFIX = "> "
    FEEDBACK_CORRECT_PREFIX = "= "
    SEPARATOR = "---"
    
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
        """Main directive handler."""
        # Validate and get question type and variant
        question_type = self.options.get("type", "multiple-choice")
        if question_type not in self.TYPES:
            raise ValueError(
                f"Unsupported question type {question_type} at line {self.lineno} in "
                f"{self.env.docname}. Supported types are: {self.TYPES}"
            )
        
        variant = self.options.get("variant", self.VARIANTS[question_type][0])
        if variant not in self.VARIANTS[question_type]:
            raise ValueError(
                f"Unsupported question variant {variant} for type {question_type} at line "
                f"{self.lineno} in {self.env.docname}. Supported variants are: "
                f"{self.VARIANTS[question_type]}"
            )
        
        columns = self.options.get("columns", self.COLUMNS[question_type][variant])
        feedback = self.options.get("feedback", self.FEEDBACKS[question_type][variant])

        # Get flags
        css_class = self.options.get("class", [])
        is_admonition = "admonition" in self.options
        no_caption = "nocaption" in self.options
        show_answer = "showanswer" in self.options

        # Create and configure node
        node = question_node()
        node["type"] = question_type
        node["variant"] = variant
        node["class"] = css_class
        node["admonition"] = is_admonition
        node["show_answer"] = show_answer
        
        # Create unique ID
        node_id = self._create_node_id()
        node["ids"] = [node_id]
        
        # Add title if provided
        if self.arguments:
            title_text = self._format_title(self.arguments[0], no_caption)
            textnodes, _ = self.state.inline_text(title_text, self.lineno)
            node_title = nodes.title(title_text, "", *textnodes, ids=[node_id + "-title"])
            node += node_title
        
        node["nocaption"] = no_caption

        # Dispatch to appropriate handler
        if question_type == "multiple-choice":
            if variant == "single-select":
                return self._handle_multiple_choice_single_select(node, node_id, columns, feedback)
            else:  # multiple-select
                return self._handle_multiple_choice_multiple_select(node, node_id, columns, feedback)
        else:  # short-answer
            return self._handle_short_answer_blocks(node, node_id, feedback)

    def _create_node_id(self) -> str:
        """Create a unique ID for the node."""
        if self.options.get("label"):
            return self.options["label"]
        # Make docname safe for HTML IDs by replacing / with -
        docname = self.env.docname.replace("/", "-")
        return f"question-{docname}-{self.env.new_serialno('question')}"

    def _format_title(self, title: str, no_caption: bool) -> str:
        """Format the title based on caption setting."""
        if no_caption:
            return title
        return f" ({title})"
            
    def _calculate_button_distribution(self, button_count: int) -> str:
        """Calculate grid distribution for buttons.
        
        Distributes buttons evenly across 4 grid positions.
        """
        if button_count == 0:
            return "1 1 1 1"
        
        positions = [1]
        if button_count > 1:
            positions.append(round(1 + (button_count - 1) / 3))
            positions.append(round(1 + 2 * (button_count - 1) / 3))
            positions.append(button_count)
        else:
            positions.extend([1, 1, 1])
        
        return " ".join(str(p) for p in positions)

    def _create_button_grid(
        self, button_dist: str, buttons: List[Tuple[str, str]]
    ) -> List[str]:
        """Create grid markup for buttons.
        
        Args:
            button_dist: Grid distribution string
            buttons: List of (css_class, label) tuples
            
        Returns:
            List of grid markup lines
        """
        grid = [f"::::{{grid}} {button_dist}", ":gutter: 3", ""]
        for css_class, label in buttons:
            grid.extend([
                ":::{grid-item-card}",
                ":shadow: lg",
                ":text-align: center",
                f":class-card: {css_class}",
                "",
                label,
                ":::",
            ])
        grid.append("::::")
        return grid

    def _add_text_section(
        self, node: Node, node_id: str, text: List[str], section_type: str
    ) -> None:
        """Add a text section to the node."""
        if text:
            section = nodes.section(
                classes=[f"question-{section_type}"],
                ids=[f"{node_id}-{section_type}"]
            )
            self.state.nested_parse(text, self.content_offset, section)
            node += section

    def _add_button_section(
        self,
        node: Node,
        node_id: str,
        buttons: List[Tuple[str, str]],
        show_answer: bool,
        button_count: int,
    ) -> None:
        """Add button section to node."""
        button_section = nodes.section(
            classes=["question-buttons"],
            ids=[f"{node_id}-buttons"]
        )
        button_dist = self._calculate_button_distribution(button_count)
        grid = self._create_button_grid(button_dist, buttons)
        self.state.nested_parse(grid, self.content_offset, button_section)
        node += button_section

    def _split_input(self) -> Tuple[List[str], List[str], List[str]]:
        """Split directive content into pre-text, options, and post-text."""
        separators = [i for i, line in enumerate(self.content) if line.strip() == self.SEPARATOR]
        
        if len(separators) < 2:
            raise ValueError(
                f"Malformed question at line {self.lineno} in {self.env.docname}. "
                f"Please provide options between '{self.SEPARATOR}' and '{self.SEPARATOR}'. "
                f"Found {len(separators)} separator(s), expected 2."
            )
        if len(separators) > 2:
            extra_lines = ", ".join(str(self.lineno + i) for i in separators[2:])
            raise ValueError(
                f"Too many separators in question at line {self.lineno} in {self.env.docname}. "
                f"Extra separators at lines: {extra_lines}"
            )
        
        pre_text = self.content[:separators[0]]
        options_raw = self.content[separators[0] + 1:separators[1]]
        post_text = self.content[separators[1] + 1:]
        
        return pre_text, options_raw, post_text

    def _handle_short_answer_blocks(self, node: Node, node_id: str, feedback: Dict) -> List[Node]:
        """Handle short-answer block questions."""
        pre_text, options_raw, post_text = self._split_input()

        # Add pre-text if present
        self._add_text_section(node, node_id, pre_text, "pretext")

        # Parse options
        options_data = self._parse_short_answer_options(options_raw, feedback, node_id)
        
        # Render options as cards
        self._render_short_answer_cards(node, node_id, options_data)

        # Add post-text if present
        self._add_text_section(node, node_id, post_text, "posttext")

        # Add buttons
        button_count = 3 if node["show_answer"] else 2
        buttons = [
            ("submit-button", "Submit answer(s)"),
        ]
        if node["show_answer"]:
            buttons.append(("show-button", "Show answer(s)"))
        buttons.append(("reset-button", "Try again"))

        self._add_button_section(node, node_id, buttons, node["show_answer"], button_count)

        return [node]

    def _parse_short_answer_options(
        self, options_raw: List[str], feedback: Dict, node_id: str
    ) -> List[Dict[str, Any]]:
        """Parse short-answer options from raw content."""
        if not options_raw:
            return []

        # Find option markers (lines starting with T[, TI[, or TF[, or M[, MR[, MNR[)
        option_starts = [
            i for i, line in enumerate(options_raw)
            if len(line.strip()) > 2 and (
                line.strip()[1:].startswith("[") or line.strip()[2:].startswith("[") or line.strip()[3:].startswith("[")
            )
        ]

        options = []
        for idx, start in enumerate(option_starts):
            end = option_starts[idx + 1] if idx + 1 < len(option_starts) else len(options_raw)
            block = options_raw[start:end]
            option = self._parse_single_short_answer_option(block, feedback)
            options.append(option)

        return options

    def _parse_single_short_answer_option(self, block: List[str], feedback: Dict) -> Dict[str, Any]:
        """Parse a single short-answer option."""
        first_line = block[0].strip()
        
        # Extract option type and answer
        option_type = first_line.split("[")[0].strip()
        answer_str = first_line.split("[")[1].split("]")[0].strip()
        
        # Extract label (text after ] on first line and subsequent lines until feedback)
        label_start = first_line.split("]", 1)[1].strip()
        label = [label_start] if label_start else []
        
        line_idx = 1
        while line_idx < len(block):
            line = block[line_idx].strip()
            if line.startswith(self.FEEDBACK_WRONG_PREFIX) or line.startswith(
                self.FEEDBACK_CORRECT_PREFIX
            ):
                break
            label.append(line)
            line_idx += 1

        # Extract feedback
        correct_fb = []
        incorrect_fb = []
        
        if line_idx < len(block):
            last_type = None
            while line_idx < len(block):
                line = block[line_idx].strip()
                if line.startswith(self.FEEDBACK_WRONG_PREFIX):
                    if incorrect_fb:
                        incorrect_fb.append("")
                    incorrect_fb.append(line[2:])
                    last_type = "incorrect"
                elif line.startswith(self.FEEDBACK_CORRECT_PREFIX):
                    if correct_fb:
                        correct_fb.append("")
                    correct_fb.append(line[2:])
                    last_type = "correct"
                else:
                    if last_type == "incorrect":
                        incorrect_fb.append(line)
                    elif last_type == "correct":
                        correct_fb.append(line)
                line_idx += 1
        else:
            correct_fb = [feedback[True]]
            incorrect_fb = [feedback[False]]

        return {
            "type": option_type,
            "answer": answer_str,
            "label": label or [""],
            "correct_feedback": correct_fb,
            "incorrect_feedback": incorrect_fb,
        }

    def _render_short_answer_cards(self, node: Node, node_id: str, options: List[Dict]) -> None:
        """Render short-answer options as cards."""
        # Create card markup
        cards_markup = []
        for option in options:
            label = option["label"]
            cards_markup.append(":::{card}")
            cards_markup.append(":shadow: lg")
            cards_markup.append(":width: 100%")
            cards_markup.append(":class-card: option")
            cards_markup.append(":class-body: input")
            if label == [""]:
                cards_markup.append(":class-header: hidden")
            cards_markup.extend(["^^^", "+++", ":::"])

        # Render cards
        options_section = nodes.section(
            classes=["question-options"],
            ids=[f"{node_id}-options"]
        )
        self.state.nested_parse(cards_markup, self.content_offset, options_section)
        node += options_section

        # Populate card content
        current_card = -1
        for container in options_section.findall(nodes.container):
            card_classes = container.get("classes", [])
            
            if "sd-card-header" in card_classes:
                current_card += 1
                option = options[current_card]
                label_section = nodes.section(
                    classes=["question-option-label"],
                    ids=[f"{node_id}-option-{current_card}-label"]
                )
                self.state.nested_parse(
                    option["label"], self.content_offset, label_section
                )
                container += label_section
                
            elif "sd-card-body" in card_classes:
                option = options[current_card]
                
                # Add input field
                if option["type"][0] == "T":
                    input_html = (
                        f"<textarea class='question-option-input type-{option['type']}' "
                        f"id='{node_id}-option-{current_card}-input' "
                        f"placeholder='Insert your answer here...'></textarea>"
                    )
                elif option["type"][0] == "M":
                    input_html = (
                        f"<math-field class='question-option-input type-{option['type']}' "
                        f"id='{node_id}-option-{current_card}-input' "
                        f"placeholder='\\text{{Insert your answer here...}}'>"
                        f"</math-field>"
                    )
                container += nodes.raw(input_html, input_html, format="html")
                
                # Add answer (hidden)
                answer_section = nodes.section(
                    classes=["question-option-answer"],
                    ids=[f"{node_id}-option-{current_card}-answer"]
                )
                answer_section += nodes.paragraph(text=option["answer"])
                container += answer_section
                
            elif "sd-card-footer" in card_classes:
                option = options[current_card]
                
                # Add correct feedback
                correct_section = nodes.section(
                    classes=["question-feedback", "correct"],
                    ids=[f"{node_id}-option-{current_card}-feedback"]
                )
                self.state.nested_parse(
                    option["correct_feedback"], self.content_offset, correct_section
                )
                container += correct_section
                
                # Add incorrect feedback
                incorrect_section = nodes.section(
                    classes=["question-feedback", "incorrect"],
                    ids=[f"{node_id}-option-{current_card}-feedback-incorrect"]
                )
                self.state.nested_parse(
                    option["incorrect_feedback"], self.content_offset, incorrect_section
                )
                container += incorrect_section
            
    def _handle_multiple_choice_shared(
        self, node: Node, node_id: str, columns: str, feedback: Dict
    ) -> Node:
        """Shared logic for multiple-choice question types."""
        pre_text, options_raw, post_text = self._split_input()

        # Parse options
        options = self._parse_multiple_choice_options(options_raw, feedback)

        # Validate (single-select requires at least one correct answer)
        if node["variant"] == "single-select" and not any(opt["is_correct"] for opt in options):
            raise ValueError(
                f"No correct options provided for single-select question at line "
                f"{self.lineno} in {self.env.docname}. Please provide at least one "
                f"correct option."
            )

        # Add pre-text
        self._add_text_section(node, node_id, pre_text, "pretext")

        # Render options as cards
        self._render_multiple_choice_cards(node, node_id, options, columns)

        # Add post-text
        self._add_text_section(node, node_id, post_text, "posttext")

        return node

    def _parse_multiple_choice_options(
        self, options_raw: List[str], feedback: Dict
    ) -> List[Dict[str, Any]]:
        """Parse multiple-choice options from raw content."""
        if not options_raw:
            return []

        # Find option markers
        option_starts = [
            i for i, line in enumerate(options_raw)
            if line.strip().startswith(self.OPTION_CHECKBOX_UNCHECKED) or
            line.strip().startswith(self.OPTION_CHECKBOX_CHECKED)
        ]

        options = []
        for idx, start in enumerate(option_starts):
            end = option_starts[idx + 1] if idx + 1 < len(option_starts) else len(options_raw)
            block = options_raw[start:end]
            option = self._parse_single_multiple_choice_option(block, feedback)
            options.append(option)

        return options

    def _parse_single_multiple_choice_option(
        self, block: List[str], feedback: Dict
    ) -> Dict[str, Any]:
        """Parse a single multiple-choice option."""
        first_line = block[0].strip()
        is_correct = first_line[1] == "x"
        
        # Extract option content and feedback
        fb_starts = [
            i for i, line in enumerate(block)
            if line.strip().startswith(self.FEEDBACK_WRONG_PREFIX)
        ]

        if fb_starts:
            fb_start = fb_starts[0]
            option_content = block[:fb_start]
            option_content[0] = option_content[0].strip()[3:]  # Remove [ ] or [x]
            option_feedback = block[fb_start:]
            option_feedback[0] = option_feedback[0].strip()[2:]  # Remove "> "
        else:
            option_content = block
            option_content[0] = option_content[0].strip()[3:]  # Remove [ ] or [x]
            option_feedback = [feedback[is_correct]]

        return {
            "is_correct": is_correct,
            "content": option_content,
            "feedback": option_feedback,
        }

    def _render_multiple_choice_cards(
        self, node: Node, node_id: str, options: List[Dict], columns: str
    ) -> None:
        """Render multiple-choice options as cards."""
        # Create card grid markup
        cards_markup = [
            f"::::{{grid}} {columns}",
            ":gutter: 3",
            "",
        ]
        for _ in options:
            cards_markup.extend([
                ":::{grid-item-card}",
                ":shadow: lg",
                ":class-card: option",
                "+++",
                ":::",
            ])
        cards_markup.append("::::")

        # Render cards
        options_section = nodes.section(
            classes=["question-options"],
            ids=[f"{node_id}-options"]
        )
        self.state.nested_parse(cards_markup, self.content_offset, options_section)
        node += options_section

        # Populate card content
        current_card = -1
        for container in options_section.findall(nodes.container):
            card_classes = container.get("classes", [])
            
            if "sd-card-body" in card_classes:
                current_card += 1
                option = options[current_card]
                option_section = nodes.section(
                    classes=["question-option"],
                    ids=[f"{node_id}-option-{current_card}"]
                )
                self.state.nested_parse(
                    option["content"], self.content_offset, option_section
                )
                container += option_section
                
            elif "sd-card-footer" in card_classes:
                option = options[current_card]
                feedback_class = "correct" if option["is_correct"] else "incorrect"
                feedback_section = nodes.section(
                    classes=["question-feedback", feedback_class],
                    ids=[f"{node_id}-feedback-{current_card}"]
                )
                self.state.nested_parse(
                    option["feedback"], self.content_offset, feedback_section
                )
                feedback_section["data-correct"] = option["is_correct"]
                container += feedback_section

    def _handle_multiple_choice_single_select(
        self, node: Node, node_id: str, columns: str, feedback: Dict
    ) -> List[Node]:
        """Handle single-select multiple-choice questions."""
        node = self._handle_multiple_choice_shared(node, node_id, columns, feedback)

        # Add buttons
        button_count = 2 if node["show_answer"] else 1
        buttons = []
        if node["show_answer"]:
            buttons.append(("show-button", "Show answer(s)"))
        buttons.append(("reset-button", "Try again"))

        self._add_button_section(node, node_id, buttons, node["show_answer"], button_count)

        return [node]

    def _handle_multiple_choice_multiple_select(
        self, node: Node, node_id: str, columns: str, feedback: Dict
    ) -> List[Node]:
        """Handle multiple-select multiple-choice questions."""
        node = self._handle_multiple_choice_shared(node, node_id, columns, feedback)

        # Add overall feedback section
        feedback_section = nodes.section(
            classes=["question-feedback", "overall-feedback"],
            ids=[f"{node_id}-overall-feedback"]
        )
        feedback_grid = [
            "::::{grid} 1",
            ":gutter: 3",
            "",
            ":::{grid-item-card}",
            ":shadow: lg",
            ":class-card: correct",
            "",
            "Well done!",
            ":::",
            ":::{grid-item-card}",
            ":shadow: lg",
            ":class-card: incorrect",
            "",
            "Try again! You selected at least one incorrect option.",
            ":::",
            ":::{grid-item-card}",
            ":shadow: lg",
            ":class-card: missed",
            "",
            "Try again! You missed at least one correct option.",
            ":::",
            "::::",
        ]
        self.state.nested_parse(feedback_grid, self.content_offset, feedback_section)
        node += feedback_section

        # Add buttons
        button_count = 3 if node["show_answer"] else 2
        buttons = [
            ("submit-button", "Submit answer(s)"),
        ]
        if node["show_answer"]:
            buttons.append(("show-button", "Show answer(s)"))
        buttons.append(("reset-button", "Try again"))

        self._add_button_section(node, node_id, buttons, node["show_answer"], button_count)

        return [node]

class question_node(nodes.Admonition, nodes.Element):
    """Custom node for question directives."""
    pass


def visit_question_node(self, node: question_node) -> None:
    """Visit handler for question nodes."""
    css_classes = " ".join(node["class"])
    css_classes += f" {node['type']} {node['variant']}"
    
    tag_name = "div"
    if node["admonition"]:
        css_classes = f"admonition {css_classes}"
    
    self.body.append(self.starttag(node, tag_name, CLASS=css_classes, ids=node["ids"]))


def depart_question_node(self, node: question_node) -> None:
    """Depart handler for question nodes."""
    if not node["nocaption"]:
        node_id = node.attributes.get("ids", [""])[0]
        search_str = f'<p class="admonition-title" id="{node_id}-title">'
        idx = _find_last_index(self.body, search_str)
        if idx >= 0:
            element = '<span class="caption-number">Question </span>'
            self.body.insert(idx + 1, element)
    
    self.body.append("</div>")


def _find_last_index(lst: List[str], value: str, skip: int = 0) -> int:
    """Find the last occurrence of a value in a list, optionally skipping occurrences.
    
    Args:
        lst: The list to search
        value: The value to find
        skip: Number of occurrences to skip from the end
        
    Returns:
        The index of the occurrence, or -1 if not found
    """
    skip_count = skip
    for i in reversed(range(len(lst))):
        if lst[i] == value:
            if skip_count == 0:
                return i
            skip_count -= 1
    return -1


def setup(app) -> Dict[str, Any]:
    """Setup function for Sphinx extension."""
    app.add_directive("question", QuestionDirective)
    app.add_node(question_node, html=(visit_question_node, depart_question_node))
    
    # Add CSS and JavaScript files
    app.add_css_file("teachbooks_questions.css")
    js_files = [
        "https://cdn.jsdelivr.net/npm/mathlive",
        "https://cdn.jsdelivr.net/npm/@cortex-js/compute-engine/dist/compute-engine.min.js",
        "teachbooks_wrapadmonition.js",
        "teachbooks_mcss.js",
        "teachbooks_mcms.js",
        "teachbooks_sab.js",
    ]
    for js_file in js_files:
        app.add_js_file(js_file)
    
    # Add static files path
    static_path = os.path.join(os.path.dirname(__file__), "_static")
    app.config.html_static_path.append(static_path)
    
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }