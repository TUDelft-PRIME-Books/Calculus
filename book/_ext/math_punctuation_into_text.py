from docutils import nodes
from sphinx.transforms import SphinxTransform

# from sphinx.util import logging
# logger = logging.getLogger(__name__)

PUNCTUATION = {".", ",", ";", ":", "!", "?"}

class InlineMathPunctuationIntoText(SphinxTransform):
    """
    Move sentence-ending punctuation immediately following inline math
    into the math content, wrapped in \\text{...}.
    """
    default_priority = 700  # After parsing, before writing

    def apply(self):
        for parent in self.document.traverse(nodes.Element):
            i = 0
            while i < len(parent.children) - 1:
                left = parent.children[i]
                right = parent.children[i + 1]

                if (
                    isinstance(left, nodes.math)
                    and isinstance(right, nodes.Text)
                    and right.strip() in PUNCTUATION
                ):
                    punct = right.strip()

                    # Modify math content
                    left.astext()  # ensure node initialized
                    left.rawsource += f"\\text{{{punct}}}"
                    left.children = []
                    left.attributes["latex"] = left.rawsource

                    # Remove punctuation text node
                    parent.remove(right)

                    # logger.info(f"Moved punctuation '{punct}' into math content at line {left.line}", color="fuchsia")
                else:
                    i += 1


def setup(app):
    app.add_transform(InlineMathPunctuationIntoText)

    return {}