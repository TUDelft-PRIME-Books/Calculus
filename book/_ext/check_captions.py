
from docutils import nodes
from sphinx.util import logging

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
            logger.info(f"No caption found for table in document {docname}.", color="yellow")
            continue

        # check if the caption ends with a .
        if not caption.astext().strip().endswith(('.', '?', '!','\\text{.}', '\\text{?}', '\\text{!}')):
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
            logger.info(f"No caption found for figure in document {docname}.", color="red")
            continue

        # check if the caption ends with a ., ? or !
        if not caption.astext().strip().endswith(('.', '?', '!','\\text{.}', '\\text{?}', '\\text{!}')):
            logger.info(f"Caption for figure in document {docname} at line {caption.line} does not end with a period: {caption.astext().strip()[-5:]}", color="blue")


def setup(app):
    app.connect("doctree-resolved", check_captions)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
