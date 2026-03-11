# _ext/numref_sections.py
from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform


# add a logger for debugging
from sphinx.util import logging
logger = logging.getLogger(__name__)

def label_for_depth(depth):
    if depth == 1:
        return "Chapter"
    elif depth == 2:
        return "Section"
    else:
        return "Subsection"

class replace_section_names(SphinxPostTransform):
    default_priority = 500
    
    def run(self, **kwargs):
        logger.info("Running replace_section_names post-transform",color='blue')

def setup(app):
    # add a post-transform that just sees of any references to sections are made and log this
    app.add_post_transform(replace_section_names)

    
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }