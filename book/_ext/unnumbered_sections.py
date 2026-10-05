from sphinx_external_toc.collectors import TocTreeCollectorWithStyles, disable_builtin_toctree_collector
from docutils import nodes
from sphinx import addnodes as sphinxnodes
import copy

class TocTreeCollectorWithUnnumbering(TocTreeCollectorWithStyles):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __renumber(self, number_set, style_set):
        if not number_set or not style_set:
            return number_set

        if not isinstance(style_set, list):
            style_set = [style_set]  # if not multiple styles are given, convert to list
        # for each style, convert the corresponding number, where only the first number
        # is rebased, the rest are kept as is, but converted.
        # convert the first number to the new style
        if style_set[0] == "numerical":
            number_set[0] = self.__numerical_count
        if style_set[0] == "romanupper":
            number_set[0] = self.__to_roman(self.__romanupper_count).upper()
        elif style_set[0] == "romanlower":
            number_set[0] = self.__to_roman(self.__romanlower_count).lower()
        elif style_set[0] == "alphaupper":
            number_set[0] = self.__to_alpha(self.__alphaupper_count).upper()
        elif style_set[0] == "alphalower":
            number_set[0] = self.__to_alpha(self.__alphalower_count).lower()
        else:
            pass
        # convert the rest of the numbers to the corresponding styles
        for i in range(1, min(len(number_set), len(style_set))):
            if style_set[i] == "numerical" and isinstance(number_set[i], int):
                continue  # keep as is
            if isinstance(number_set[i], str):
                continue  # skip non-numeric values, assuming those are already converted
            if style_set[i] == "romanupper":
                number_set[i] = self.__to_roman(int(number_set[i])).upper()
            elif style_set[i] == "romanlower":
                number_set[i] = self.__to_roman(int(number_set[i])).lower()
            elif style_set[i] == "alphaupper":
                number_set[i] = self.__to_alpha(int(number_set[i])).upper()
            elif style_set[i] == "alphalower":
                number_set[i] = self.__to_alpha(int(number_set[i])).lower()
            else:
                pass

        return number_set

    def __fix_nested_toc(self, env, toctree, style):
        for _, ref in toctree["entries"]:
            # Only process internal document references
            if ref not in env.titles:
                continue

            if "secnumber" not in env.titles[ref]:
                continue
            new_secnumber = self.__renumber(env.titles[ref]["secnumber"], style)
            env.titles[ref]["secnumber"] = copy.deepcopy(new_secnumber)
            if ref in env.tocs:
                self._replace_toc(env, ref, env.tocs[ref], style)

    def _replace_toc(self, env, ref, node, style):
        if isinstance(node, nodes.reference):
            if style == "unnumbered":
                if "secnumber" in node:
                    del node["secnumber"]
            else:
                fixed_number = self.__renumber(node["secnumber"], style)
                node["secnumber"] = fixed_number
                env.toc_secnumbers[ref][node["anchorname"]] = fixed_number

        elif isinstance(node, sphinxnodes.toctree):
            self.__fix_nested_toc(env, node, style)

        else:
            for child in node.children:
                self._replace_toc(env, ref, child, style)

    def assign_section_numbers(self, env):
        # First, call the original assign_section_numbers to get the default behavior
        result = super().assign_section_numbers(env)  # needed to maintain functionality

        # try to see if we can find the title nodes belonging to a title
        docnames_to_filter = []
        for docname in env.toc_secnumbers:
            for anchorname, secnumber in env.toc_secnumbers[docname].items():
                if not anchorname: # only do things at the top level (i.e. document level)
                    title_node = find_title_for_anchor(env,docname,anchorname)
                    if title_node:
                        # get the parent if any
                        parent_node = title_node.parent
                        if parent_node:
                            # check if it should be unnumbered
                            if "classes" in parent_node:
                                if "unnumbered" in parent_node["classes"]:
                                    env.toc_secnumbers[docname][anchorname] = None
                                    other_title_node = env.titles[docname]
                                    del other_title_node["secnumber"]
                                    docnames_to_filter.append(docname)
                                    if docname in env.tocs:
                                        self._replace_toc(env, docname, env.tocs[docname], "unnumbered")
                                    
        try_again = True
        while try_again:
            docnames_to_filter_set = set(docnames_to_filter)
            for docname in docnames_to_filter:
                children = env.toctree_includes.get(docname, [])
                for child in children:
                    docnames_to_filter_set.add(child)
            if len(docnames_to_filter_set) == len(docnames_to_filter):
                try_again = False
            else:
                docnames_to_filter = list(docnames_to_filter_set)
        docnames_to_filter = list(docnames_to_filter_set)
        
        for docname in docnames_to_filter:
            for anchor in env.toc_secnumbers[docname]:
                env.toc_secnumbers[docname][anchor] = None

        return result

def setup(app) -> dict:
    app.setup_extension("sphinx_external_toc")

    # collectors
    disable_builtin_toctree_collector(app)
    app.add_env_collector(TocTreeCollectorWithUnnumbering)

    return {"version": 'built-in', "parallel_read_safe": True}

def find_title_for_anchor(env, docname, anchorname):
    doctree = env.get_doctree(docname)

    # document title
    if not anchorname:
        return doctree.next_node(nodes.title)

    anchor = anchorname.lstrip("#")

    for section in doctree.findall(nodes.section):
        if anchor in section["ids"]:
            return section[0] if isinstance(section[0], nodes.title) else section.next_node(nodes.title)

    return None