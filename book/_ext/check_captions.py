
from docutils import nodes
from sphinx.util import logging
from teachbooks_sphinx_grasple.nodes import grasple_exercise_enumerable_node

logger = logging.getLogger(__name__)

def check_captions(app, doctree, docname):
    """
    After Sphinx has created the doctree, walk through all table and figure nodes
    And check if they have a caption. If not, log a warning.
    """

    for table in doctree.findall(nodes.table):
        # Find caption node
        caption = None
        for child in table.children:
            if isinstance(child, nodes.title):
                caption = child
                break

        # If no caption → nothing to do
        if caption is None:
            logger.info(f"No caption found for table in document {docname} at line {table.line}.", color="yellow")
            continue

        # check if the caption ends with a .
        if not caption.astext().strip().endswith(('.', '?', '!','\\text{.}', '\\text{?}', '\\text{!}')):
            if caption.line is not None:
                logger.info(f"Caption for table in document {docname} at line {caption.line} does not end with a period.", color="green")

    for figure in doctree.findall(nodes.figure):
        # Find caption node
        caption = None
        for child in figure.children:
            if isinstance(child, nodes.caption):
                caption = child
                break

        # If no caption → nothing to do
        if caption is None:
            logger.info(f"No caption found for figure in document {docname} at line {figure.line}.", color="red")
            continue

        # check if the caption ends with a ., ? or !
        if not caption.astext().strip().endswith(('.', '?', '!','\\text{.}', '\\text{?}', '\\text{!}')):
            if caption.line is not None:
                logger.info(f"Caption for figure in document {docname} at line {caption.line} does not end with a period: {caption.astext().strip()[-5:]}", color="blue")

    for grasple in doctree.findall(grasple_exercise_enumerable_node):
        # extract description from grasple node
        description = None
        for child in grasple.findall(nodes.container):
            if 'description-container' in child.attributes.get('classes', []):
                description = child
                break

        # If no description → nothing to do
        if description is None:
            logger.info(f"No description found for grasple exercise in document {docname} at line {grasple.line}.", color="fuchsia")
            continue
        if not description.astext().strip():
            logger.info(f"No or empty description found for grasple exercise in document {docname} at line {grasple.line}.", color="fuchsia")
            continue

        description_text = description.astext()
        # check if the description ends with a ., ? or !
        if not description_text.endswith(('.', '?', '!','\\text{.}', '\\text{?}', '\\text{!}')):
            # if description.line is not None:
            logger.info(f"Description for grasple exercise in document {docname} at line {grasple.line} does not end with a period: {description.astext().strip()[-5:]}", color="teal")


def setup(app):
    app.connect("doctree-resolved", check_captions)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
