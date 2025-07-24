"""
sphinx_code_examples.nodes
"""

from sphinx.util import logging
from docutils.nodes import Node
from docutils import nodes as docutil_nodes
from sphinx import addnodes as sphinx_nodes
from sphinx.writers.latex import LaTeXTranslator
from .latex import LaTeXMarkup

logger = logging.getLogger(__name__)
LaTeX = LaTeXMarkup()


# Nodes


class codex_node(docutil_nodes.Admonition, docutil_nodes.Element):
    gated = False


class codex_enumerable_node(docutil_nodes.Admonition, docutil_nodes.Element):
    gated = False
    resolved_title = False


class codex_end_node(docutil_nodes.Admonition, docutil_nodes.Element):
    pass

class codex_title(docutil_nodes.title):
    def default_title(self):
        title_text = self.children[0].astext()
        if title_text == "Codex" or title_text == "Codex %s":
            return True
        else:
            return False


class codex_subtitle(docutil_nodes.subtitle):
    pass

class codex_latex_number_reference(sphinx_nodes.number_reference):
    pass


# Test Node Functions


def is_codex_node(node):
    return isinstance(node, codex_node) or isinstance(node, codex_enumerable_node)


def is_codex_enumerable_node(node):
    return isinstance(node, codex_enumerable_node)

def is_extension_node(node):
    return (
        is_codex_node(node)
        or is_codex_enumerable_node(node)
    )


# Visit and Depart Functions


def visit_codex_node(self, node: Node) -> None:
    if isinstance(self, LaTeXTranslator):
        label = (
            "\\phantomsection \\label{" + f"codex:{node.attributes['label']}" + "}"
        )  # TODO: Check this resolves.
        self.body.append(label)
        self.body.append(LaTeX.visit_admonition())
    else:
        self.body.append(self.starttag(node, "div", CLASS="admonition"))
        self.body.append("\n")


def depart_codex_node(self, node: Node) -> None:
    if isinstance(self, LaTeXTranslator):
        self.body.append(LaTeX.depart_admonition())
    else:
        self.body.append("</div>")


def visit_codex_enumerable_node(self, node: Node) -> None:
    """
    LaTeX Reference Structure is codex:{label} and resolved by
    codex_latex_number_reference nodes (see below)
    """
    if isinstance(self, LaTeXTranslator):
        label = (
            "\\phantomsection \\label{" + f"codex:{node.attributes['label']}" + "}\n"
        )
        self.body.append(label)
        self.body.append(LaTeX.visit_admonition())
    else:
        self.body.append(self.starttag(node, "div", CLASS="admonition"))
        self.body.append("\n")


def depart_codex_enumerable_node(self, node: Node) -> None:
    if isinstance(self, LaTeXTranslator):
        self.body.append(LaTeX.depart_admonition())
    else:
        self.body.append("</div>")
        self.body.append("\n")

def visit_codex_latex_number_reference(self, node):
    id = node.get("refid")
    text = node.astext()
    hyperref = r"\hyperref[codex:%s]{%s}" % (id, text)
    self.body.append(hyperref)
    raise docutil_nodes.SkipNode


def depart_codex_latex_number_reference(self, node):
    pass
