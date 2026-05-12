import os

from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList
from docutils import nodes

from sphinx.util import logging
logger = logging.getLogger(__name__)

LIST_OF_LINK_ROLES = ["ref", "numref", "prf:ref","bdg-link"]

class FetchDirective(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "class": directives.class_option,
        "title": directives.unchanged
        }

    def run(self):
        # get the argument and do a sanity check
        if not self.arguments:
            raise self.error("The 'fetch' directive requires an argument.")
        sane_argument = False
        # check if the argument is a markdown link with an id
        if self.arguments[0].startswith("[") and "](" in self.arguments[0] and "#" in self.arguments[0] and self.arguments[0].endswith(")"):
            sane_argument = True
        # check if the argument is a myst reference role
        if self.arguments[0].startswith("{") and "}`" in self.arguments[0] and self.arguments[0].endswith("`"):
            for role in LIST_OF_LINK_ROLES:
                if self.arguments[0].startswith("{" + role):
                    sane_argument = True
                    break
        # check if the argument is a rst reference role
        if self.arguments[0].startswith(":") and ":`" in self.arguments[0] and self.arguments[0].endswith("`"):
            for role in LIST_OF_LINK_ROLES:
                if self.arguments[0].startswith(":" + role):
                    sane_argument = True
                    break
        # check if it is a html link
        if self.arguments[0].startswith("<a ") and "href=" in self.arguments[0] and self.arguments[0].endswith("</a>"):
            sane_argument = True

        if not sane_argument:
            raise self.error("The argument of the 'fetch' directive must be a markdown link, a reference, or an HTML link.")

        # Get and build the class list
        if "class" in self.options:
            classes = "fetch " + " ".join(self.options["class"])
        else:
            classes = "fetch"

        # Get and build the content
        if self.content:
            content = self.content
            if isinstance(content, str):
                content = [content]
            elif not isinstance(content, list):
                content = list(content)
        else:
            content = ["Content loading..."]
        content = [line.replace("[!a!]", self.arguments[0]) for line in content]

        # Get and build the title
        if "title" in self.options:
            title = self.options["title"]
        else:
            title = "Fetching [!a!]"
        title = title.replace("[!a!]", self.arguments[0])
        
        # create dummy code
        code = [f":::{{admonition}} {title}",
                f":class: {classes}"]
        code += content
        code.append(":::")
        
        # Parse the code into nodes
        node = nodes.container()
        self.state.nested_parse(StringList(code), 0, node)
        
        return [node.children[0]]
    
class ClickToFetchDirective(FetchDirective):
    # differences are:
    # - the additional class "click-to-fetch"
    # - the default title is "Click to fetch [!a!]" instead of "Fetching [!a!]"
    # - the default content is "Waiting for a click..." instead of "Content loading..."
    def run(self):
        # add "click-to-fetch" to the class list
        if "class" in self.options:
            self.options["class"].append("click-to-fetch")
        else:
            self.options["class"] = ["click-to-fetch"]
        # change the default title
        if "title" not in self.options:
            self.options["title"] = "Click to fetch [!a!]"
        # change the default content
        if "content" not in self.options:
            self.options["content"] = ["Waiting for a click..."]
        
        return super().run()

def on_builder_inited(app):
    """Register the static directory so its files are copied to the build output."""
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if static_dir not in app.config.html_static_path:
        app.config.html_static_path.append(static_dir)

def inject_assets(app, pagename, templatename, context, doctree):
    app.add_css_file('teachbooks_fetch.css')
    app.add_js_file('teachbooks_fetch.js')

def setup(app):
    app.add_directive("fetch", FetchDirective)
    app.add_directive("click-to-fetch", ClickToFetchDirective)
    app.connect('builder-inited', on_builder_inited)
    app.connect('html-page-context', inject_assets)

    return {"version": "0.1", "parallel_read_safe": True}
