from docutils import nodes
from sphinx.util import logging
import os

logger = logging.getLogger(__name__)

def check_images(app, exception):
    """
    After Sphinx has finished building, walk through all doctrees
    collect all image URIs.

    Compare this list of URIs with the list of files in the source directory.
    If there are any files that do not correspond to a URI, log a warning.
    """
    
    if exception is not None:
        return
    
    # Collect all image URIs from all doctrees
    image_uris = set()
    for docname in app.env.found_docs:
        doctree = app.env.get_doctree(docname)
        for img_node in doctree.traverse(nodes.image):
            uri = img_node['uri']
            image_uris.add(uri)
    
    # Get source directory
    source_dir = app.srcdir
    
    # Walk through source directory and collect all image files
    image_files = set()
    for root, dirs, files in os.walk(source_dir):
        # Remove folders starting with _ from traversal
        dirs[:] = [d for d in dirs if not d.startswith('_')]
        
        for file in files:
            # Check for common image extensions
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')):
                rel_path = os.path.relpath(os.path.join(root, file), source_dir)
                # Normalize path separators for comparison
                rel_path = rel_path.replace(os.sep, '/')
                image_files.add(rel_path)
    
    # Find unused images
    unused_images = image_files - image_uris
    for img in sorted(unused_images):
        logger.info(f"Unused image file: {img}",color="fuchsia")


def setup(app):
    app.connect("build-finished", check_images)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
