from docutils import nodes
from sphinx.transforms import SphinxTransform

PUNCTUATION = {".", ",", ";", ":", "!", "?"}

class InlineMathPunctuationIntoText(SphinxTransform):
    """
    Move sentence-ending punctuation immediately following inline math
    into the math content, wrapped in \\text{...}.
    """
    default_priority = 700  # After parsing, before writing

    def apply(self):
        for math in self.document.findall(nodes.math):
            # get the next node inside the parent
            parent = math.parent
            if parent is not None:
                index = parent.index(math)
                if index + 1 < len(parent):
                    next_node = parent[index + 1]
                    if next_node and isinstance(next_node, nodes.Text):
                        text = next_node.astext()
                        if text and text[0] in PUNCTUATION:
                            punctuation = text[0]
                            new_latex = f"{math.astext()}\\text{{{punctuation}}}"
                            new_math = nodes.math(new_latex, new_latex)
                            math.replace_self(new_math)
                            new_text = text[1:]  # Remove the punctuation
                            if new_text:
                                new_next_node = nodes.Text(new_text)
                                idx_next = parent.index(next_node)
                                parent[idx_next] = new_next_node
                            else:
                                next_node.parent.remove(next_node)
                            
        # raise Exception()

def setup(app):
    app.add_transform(InlineMathPunctuationIntoText)

    return {}