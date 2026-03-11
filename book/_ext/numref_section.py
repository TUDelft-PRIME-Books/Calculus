# _ext/numref_sections.py

from __future__ import annotations
from typing import Optional, Tuple
from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.addnodes import pending_xref

from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform


# # add a logger for debugging
# from sphinx.util import logging
# logger = logging.getLogger(__name__)

class replace_section_names(SphinxPostTransform):
    default_priority = 500

    def run(self, **kwargs):
        
        env = self.env
        app = self.app

        for ref in self.document.findall(nodes.reference):
            # if the title contains "Section " followed by a label, replace it with "Chapter" (as a test)
            # only apply to internal references (those with a refid)
            if not ref.get("internal"):
                continue
            # only apply if a title with Section is included
            if not ref.get("title") or "Section " not in ref["title"]:
                continue
            # only apply to numref results
            child = ref.children[0] if ref.children else None
            if child is None or not isinstance(child, nodes.inline):
                continue
            if not child.get("classes") or "std-numref" not in child["classes"]:
                continue
            # logger.info(f"Checking node:\n{ref.pformat()}",color='blue')
            # extract the real label from the rendered title (assuming it's of the form "Section <label>")
            label = child.astext().replace("Section ","")
            # use number of . in the label to determine if it's a chapter, a section or a subsection
            count = label.count(".")
            if count == 0:
                # a chapter, so replace with "Chapter"
                child.clear()
                child += nodes.Text(f"Chapter {label}")
                ref["title"] = ref["title"].replace("Section ","Chapter ")
            elif count >= 2:
                # a subsection or deeper, so replace with "Subsection"
                child.clear()
                child += nodes.Text(f"Subsection {label}")
                ref["title"] = ref["title"].replace("Section ","Subsection ")
            # other wise a section, so keep as is.



def setup(app):
    # add a post-transform that just sees of any references to sections are made and log this
    app.add_post_transform(replace_section_names)

    
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }