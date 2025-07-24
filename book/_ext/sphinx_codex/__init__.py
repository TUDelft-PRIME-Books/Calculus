# -*- coding: utf-8 -*-
"""
sphinx_code_examples
~~~~~~~~~~~~~~~~~~~~

This package is an extension for sphinx to support examples with runnable code.

"""

from pathlib import Path
from typing import Any, Dict, Set, Union, cast
from sphinx.config import Config
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.domains.std import StandardDomain
from docutils.nodes import Node
from sphinx.util import logging
from sphinx.util.fileutil import copy_asset
import re

from ._compat import findall
from .directive import (
    CodexDirective,
    CodexStartDirective,
    CodexEndDirective,
)
from .nodes import (
    codex_node,
    visit_codex_node,
    depart_codex_node,
    codex_enumerable_node,
    visit_codex_enumerable_node,
    depart_codex_enumerable_node,
    codex_end_node,
    is_extension_node,
    codex_title,
    codex_subtitle,
    codex_latex_number_reference,
    visit_codex_latex_number_reference,
    depart_codex_latex_number_reference,
)
from .transforms import (
    CheckGatedDirectives,
    MergeGatedCodexs,
)
from .post_transforms import (
    ResolveTitlesInCodexs,
    UpdateReferencesToEnumerated,
)

logger = logging.getLogger(__name__)


# Callback Functions


def purge_codexs(app: Sphinx, env: BuildEnvironment, docname: str) -> None:
    """Purge sphinx_codex registry"""

    if not hasattr(env, "sphinx_codex_registry"):
        return

    # Purge env.sphinx_codex_registry if matching docname
    remove_labels = [
        label
        for (label, node) in env.sphinx_codex_registry.items()
        if node["docname"] == docname
    ]
    if remove_labels:
        for label in remove_labels:
            del env.sphinx_codex_registry[label]


def merge_codexs(
    app: Sphinx, env: BuildEnvironment, docnames: Set[str], other: BuildEnvironment
) -> None:
    """Merge sphinx_codex_registry"""

    if not hasattr(env, "sphinx_codex_registry"):
        env.sphinx_codex_registry = {}

    # Merge env stored data
    if hasattr(other, "sphinx_codex_registry"):
        env.sphinx_codex_registry = {
            **env.sphinx_codex_registry,
            **other.sphinx_codex_registry,
        }


def init_numfig(app: Sphinx, config: Config) -> None:
    """Initialize numfig"""

    config["numfig"] = True
    numfig_format = {"codex": f"{app.config.sphinx_codex_name} %s"}
    # Merge with current sphinx settings
    numfig_format.update(config.numfig_format)
    config.numfig_format = numfig_format

def doctree_read(app: Sphinx, document: Node) -> None:
    """
    Read the doctree and apply updates to sphinx-codex nodes
    """

    domain = cast(StandardDomain, app.env.get_domain("std"))

    # Traverse sphinx-codex nodes
    for node in findall(document):
        if is_extension_node(node):
            name = node.get("names", [])[0]
            label = document.nameids[name]
            docname = app.env.docname
            section_name = node.attributes.get("title")
            domain.anonlabels[name] = docname, label
            domain.labels[name] = docname, label, section_name

def on_config_inited(app: Sphinx, config: Config) -> None:
    check_config(app, config)
    init_numfig(app, config)

def check_config(app: Sphinx, config: Config) -> None:
    # check validity of config  and act accordingly
    if config.sphinx_codex_merge_with_proof:
        if config.sphinx_codex_name == "":
            config.sphinx_codex_name = "Example"
        config.sphinx_codex_style_from_proof = True
        config.sphinx_codex_icon_from_proof = True
    else:
        if config.sphinx_codex_name == "":
            config.sphinx_codex_name = "Code example"

def on_source_read_replace_prf_example(app, docname, source):

    if app.config.sphinx_codex_merge_with_proof:
        # If the config is set to merge with proof, replace 'prf:example' with 'codex'

        # Get the source text
        text = source[0]
        
        # Check if this is a Jupyter notebook by looking at the source file
        # Since docname doesn't include extension, we need to check the app's source file
        is_notebook = False
        if hasattr(app.env, 'found_docs') and docname in app.env.found_docs:
            # Try to get the actual source file path
            src_path = app.env.doc2path(docname, base=False)
            is_notebook = src_path.endswith('.ipynb')
                
        # Initialize tracking of example labels if not exists
        if not hasattr(app.env, 'codex_example_labels'):
            app.env.codex_example_labels = set()
        
        # Find all labels from {prf:example} directives and track them
        example_pattern = re.compile(r'\{prf:example\}.*?:label:\s*([^\s\n]+)', re.DOTALL)
        for match in example_pattern.finditer(text):
            label = match.group(1).strip()  # Remove whitespace and newlines
            if is_notebook:
                label = label.replace("\\n\",", "")
            app.env.codex_example_labels.add(label)
        
        # Replace all occurrences of '{prf:example}' with '{codex}' in directive contexts
        text = text.replace('{prf:example}', '{codex}')

        # Replace all occurrences of '{prf:ref}`[^`]label[^`]' with '{numref}`[^`]label[^`]`'
        if hasattr(app.env, 'codex_example_labels'):
            for label in app.env.codex_example_labels:
                # Create a regex pattern to match the specific label
                label_pattern = re.compile(r"\{prf:ref\}(`[^`]*"+re.escape(label)+"[^`]*`)", re.DOTALL)
                for match in label_pattern.finditer(text):
                    text = text.replace(match.group(0), f'{{numref}}{match.group(1)}')

        source[0] = text

def setup(app: Sphinx) -> Dict[str, Any]:
    app.setup_extension("sphinx_proof")

    app.add_config_value("sphinx_codex_name", "", "html")
    app.add_config_value("sphinx_codex_style_from_proof", True, "html")
    app.add_config_value("sphinx_codex_icon_from_proof", False, "html")
    app.add_config_value("sphinx_codex_merge_with_proof", False, "html")

    app.connect("config-inited", on_config_inited)  # event order - 1
    app.connect("builder-inited", set_asset_files)  # event order - 2
    app.connect("env-purge-doc", purge_codexs)  # event order - 5 per file
    app.connect("source-read", on_source_read_replace_prf_example) # event order - 6 per file
    app.connect("doctree-read", doctree_read)  # event order - 8
    app.connect("env-merge-info", merge_codexs)  # event order - 9
    app.connect("build-finished", copy_asset_files)  # event order - 16

    app.add_node(
        codex_node,
        singlehtml=(visit_codex_node, depart_codex_node),
        html=(visit_codex_node, depart_codex_node),
        latex=(visit_codex_node, depart_codex_node),
    )

    app.add_enumerable_node(
        codex_enumerable_node,
        "codex",
        None,
        singlehtml=(visit_codex_enumerable_node, depart_codex_enumerable_node),
        html=(visit_codex_enumerable_node, depart_codex_enumerable_node),
        latex=(visit_codex_enumerable_node, depart_codex_enumerable_node),
    )

    # Internal Title Nodes that don't need visit_ and depart_ methods
    # as they are resolved in post_transforms to docutil and sphinx nodes
    app.add_node(codex_end_node)
    app.add_node(codex_title)
    app.add_node(codex_subtitle)

    app.add_node(
        codex_latex_number_reference,
        latex=(
            visit_codex_latex_number_reference,
            depart_codex_latex_number_reference,
        ),
    )

    app.add_directive("codex", CodexDirective)
    app.add_directive("codex-start", CodexStartDirective)
    app.add_directive("codex-end", CodexEndDirective)

    app.add_transform(CheckGatedDirectives)
    app.add_transform(MergeGatedCodexs)

    app.add_post_transform(UpdateReferencesToEnumerated)
    app.add_post_transform(ResolveTitlesInCodexs)

    return {
        "version": "builtin",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

def set_asset_files(app: Sphinx) -> None:
    """Sets the asset files for the codex extension"""

    if not(app.config.sphinx_codex_icon_from_proof):
        app.add_css_file("codex.css")

def copy_asset_files(app: Sphinx, exc: Union[bool, Exception]):
    """Copies required assets for formating in HTML"""

    if not(app.config.sphinx_codex_icon_from_proof):

        static_path = (
            Path(__file__).parent.joinpath("assets", "html", "codex.css").absolute()
        )
        asset_files = [str(static_path)]

        if exc is None:
            for path in asset_files:
                copy_asset(path, str(Path(app.outdir).joinpath("_static").absolute()))