# -*- coding: utf-8 -*-
"""
sphinx_codex
~~~~~~~~~~~~~~~
This package is an extension for sphinx to support codex and solutions.
:copyright: Copyright 2020-2021 by the Executable Books team, see AUTHORS.
:license: MIT, see LICENSE for details.
"""

__version__ = "1.0.1"

from pathlib import Path
from typing import Any, Dict, Set, Union, cast
from sphinx.config import Config
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.domains.std import StandardDomain
from docutils.nodes import Node
from sphinx.util import logging
from sphinx.util.fileutil import copy_asset

from ._compat import findall
from .directive import (
    CodexDirective,
    CodexStartDirective,
    CodexEndDirective,
    SolutionDirective,
    SolutionStartDirective,
    SolutionEndDirective,
)
from .nodes import (
    codex_node,
    visit_codex_node,
    depart_codex_node,
    codex_enumerable_node,
    visit_codex_enumerable_node,
    depart_codex_enumerable_node,
    codex_end_node,
    solution_node,
    visit_solution_node,
    depart_solution_node,
    solution_start_node,
    solution_end_node,
    is_extension_node,
    codex_title,
    codex_subtitle,
    solution_title,
    solution_subtitle,
    codex_latex_number_reference,
    visit_codex_latex_number_reference,
    depart_codex_latex_number_reference,
)
from .transforms import (
    CheckGatedDirectives,
    MergeGatedSolutions,
    MergeGatedCodexs,
)
from .post_transforms import (
    ResolveTitlesInCodexs,
    ResolveTitlesInSolutions,
    UpdateReferencesToEnumerated,
    ResolveLinkTextToSolutions,
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
    numfig_format = {"codex": "Code example %s"}
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


def setup(app: Sphinx) -> Dict[str, Any]:
    # app.add_config_value("hide_solutions", False, "env")

    app.connect("config-inited", init_numfig)  # event order - 1
    app.connect("env-purge-doc", purge_codexs)  # event order - 5 per file
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

    # app.add_node(
    #     solution_node,
    #     singlehtml=(visit_solution_node, depart_solution_node),
    #     html=(visit_solution_node, depart_solution_node),
    #     latex=(visit_solution_node, depart_solution_node),
    # )

    # Internal Title Nodes that don't need visit_ and depart_ methods
    # as they are resolved in post_transforms to docutil and sphinx nodes
    app.add_node(codex_end_node)
    # app.add_node(solution_start_node)
    # app.add_node(solution_end_node)
    app.add_node(codex_title)
    app.add_node(codex_subtitle)
    # app.add_node(solution_title)
    # app.add_node(solution_subtitle)

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
    # app.add_directive("solution", SolutionDirective)
    # app.add_directive("solution-start", SolutionStartDirective)
    # app.add_directive("solution-end", SolutionEndDirective)

    app.add_transform(CheckGatedDirectives)
    app.add_transform(MergeGatedCodexs)
    app.add_transform(MergeGatedSolutions)

    app.add_post_transform(UpdateReferencesToEnumerated)
    app.add_post_transform(ResolveTitlesInCodexs)
    app.add_post_transform(ResolveTitlesInSolutions)
    app.add_post_transform(ResolveLinkTextToSolutions)

    app.add_css_file("codex.css")

    return {
        "version": "builtin",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

def copy_asset_files(app: Sphinx, exc: Union[bool, Exception]):
    """Copies required assets for formating in HTML"""

    static_path = (
        Path(__file__).parent.joinpath("assets", "html", "codex.css").absolute()
    )
    asset_files = [str(static_path)]

    if exc is None:
        for path in asset_files:
            copy_asset(path, str(Path(app.outdir).joinpath("_static").absolute()))