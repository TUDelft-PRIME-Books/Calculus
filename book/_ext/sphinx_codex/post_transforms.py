"""
sphinx_code_examples.post_transforms
"""

import sphinx.addnodes as sphinx_nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from docutils import nodes as docutil_nodes

from ._compat import findall
from .utils import get_node_number
from .nodes import (
    codex_enumerable_node,
    codex_title,
    codex_subtitle,
    is_codex_node,
)

logger = logging.getLogger(__name__)


def build_reference_node(app, target_node):
    """
    Builds a docutil.nodes.reference object
    to a given target_node.
    """
    refuri = app.builder.get_relative_uri(
        app.env.docname, target_node.get("docname", "")
    )
    refuri += "#" + target_node.get("label")
    reference = docutil_nodes.reference(
        "",
        "",
        internal=True,
        refuri=refuri,
        anchorname="",
    )
    return reference


class UpdateReferencesToEnumerated(SphinxPostTransform):
    """
        Updates all :ref: to :numref: if used when referencing
        an enumerated codex node.
    ]"""

    default_priority = 5

    def run(self):
        if not hasattr(self.env, "sphinx_codex_registry"):
            return

        for node in findall(self.document, sphinx_nodes.pending_xref):
            if node.get("reftype") != "numref":
                target_label = node.get("reftarget")
                if target_label in self.env.sphinx_codex_registry:
                    target = self.env.sphinx_codex_registry[target_label]
                    target_node = target.get("node")
                    if isinstance(target_node, codex_enumerable_node):
                        # Don't Modify Custom Text
                        if node.get("refexplicit"):
                            continue
                        node["reftype"] = "numref"
                        node['refdomain'] = 'std'
                        # Get Metadata from Inline
                        inline = node.children[0]
                        classes = inline["classes"]
                        if "std-ref" in classes:
                            classes.remove("std-ref")
                            classes.append("std-numref")
                        elif "prf-ref" in classes:
                            classes.remove("prf")
                            classes.remove("prf-ref")
                            classes.append("std")
                            classes.append("std-numref")
                        else:
                            msg = f"Pending xref found without 'std-ref' or 'prf-ref':\nNode: {node}"
                            docpath = self.env.doc2path(self.env.docname)
                            path = docpath[: docpath.rfind(".")]
                            logger.warning(msg, location=path, color="red")
                        # Construct a Literal Node
                        literal = docutil_nodes.literal()
                        literal["classes"] = classes
                        literal.children += inline.children
                        node.children[0] = literal


class ResolveTitlesInCodexs(SphinxPostTransform):
    """
    Resolve Titles for Codex Nodes and Enumerated Codex Nodes
    for:
        1. Numbering
        2. Formatting Title and Subtitles into docutils.title node
    """

    default_priority = 20

    def resolve_title(self, node):
        title = node.children[0]
        if isinstance(title, codex_title):
            updated_title = docutil_nodes.title()
            if isinstance(node, codex_enumerable_node):
                # Numfig (HTML) will use "Codex %s" so we just need the subtitle
                if self.app.builder.format == "latex":
                    # Resolve Title
                    node_number = get_node_number(self.app, node, "codex")
                    title_text = self.app.config.numfig_format["codex"] % node_number
                    updated_title += docutil_nodes.Text(title_text)
                updated_title["title"] = self.app.config.numfig_format["codex"]
            else:
                # Use default text "Codex"
                updated_title += title.children[0]
            # Parse Custom Titles
            if len(title.children) > 1:
                subtitle = title.children[1]
                if isinstance(subtitle, codex_subtitle):
                    updated_title += docutil_nodes.Text(" (")
                    for child in subtitle.children:
                        updated_title += child
                    updated_title += docutil_nodes.Text(")")
            updated_title.parent = title.parent
            node.children[0] = updated_title
        node.resolved_title = True
        return node

    def run(self):
        if not hasattr(self.env, "sphinx_codex_registry"):
            return

        for node in findall(self.document, is_codex_node):
            node = self.resolve_title(node)
