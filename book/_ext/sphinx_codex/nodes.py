"""
sphinx_codex.nodes
~~~~~~~~~~~~~~~~~~~~~

Sphinx Codex Nodes

:copyright: Copyright 2020-2021 by the Executable Books team, see AUTHORS
:licences: see LICENSE for details
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


class solution_node(docutil_nodes.Admonition, docutil_nodes.Element):
    resolved_title = False


class solution_start_node(docutil_nodes.Admonition, docutil_nodes.Element):
    resolved_title = False


class solution_end_node(docutil_nodes.Admonition, docutil_nodes.Element):
    resolved_title = False  # TODO: is this required?


class codex_title(docutil_nodes.title):
    def default_title(self):
        title_text = self.children[0].astext()
        if title_text == "Codex" or title_text == "Codex %s":
            return True
        else:
            return False


class codex_subtitle(docutil_nodes.subtitle):
    pass


class solution_title(docutil_nodes.title):
    def default_title(self):
        title_text = self.children[0].astext()
        if title_text == "Solution to":
            return True
        else:
            return False


class solution_subtitle(docutil_nodes.subtitle):
    pass


class codex_latex_number_reference(sphinx_nodes.number_reference):
    pass


# Test Node Functions


def is_codex_node(node):
    return isinstance(node, codex_node) or isinstance(node, codex_enumerable_node)


def is_codex_enumerable_node(node):
    return isinstance(node, codex_enumerable_node)


def is_solution_node(node):
    return isinstance(node, solution_node)


def is_extension_node(node):
    return (
        is_codex_node(node)
        or is_codex_enumerable_node(node)
        or is_solution_node(node)
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


def visit_solution_node(self, node: Node) -> None:
    """
    Reference Structure is {docname}:{label} and resolved by Sphinx
    """
    if isinstance(self, LaTeXTranslator):
        target_label = node.attributes["label"]
        target_node = self.builder.env.sphinx_codex_registry[target_label]
        docname = target_node.get("docname")
        label = (
            "\\phantomsection \\label{"
            + f"{docname}:{node.attributes['label']}"
            + "}\n"
        )
        self.body.append(label)
        self.body.append(LaTeX.visit_admonition())
    else:
        self.body.append(self.starttag(node, "div", CLASS="admonition"))
        self.body.append("\n")


def depart_solution_node(self, node: Node) -> None:
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
