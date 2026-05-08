from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList
from docutils import nodes


class RepeatDirective(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    option_spec = {"manual": directives.flag}

    def run(self):
        text = self.arguments[0]
        
        # Validate that the argument is a valid reference
        valid_refs = ('{numref}', '{ref}', '{prf:ref}')
        if not any(text.startswith(ref) for ref in valid_refs):
            raise self.error(f"repeat directive argument must start with one of: {', '.join(valid_refs)}")
        
        # Build the class list
        classes = "repeat"
        if "manual" in self.options:
            classes += ", manual"
        # build the content
        content = ""
        if "manual" not in self.options:
            content = "Content loading..."
        else:
            content = f"Click to load content."
        # build the title
        if "manual" in self.options:
            title = "Placeholder for repeated "
        else:
            title = "Repeating "
        
        # create dummy code
        code = [f":::{{admonition}} {title}{text}",
                f":class: {classes}",
                f"{content}",
                ":::"]
        
        # Parse the code into nodes
        node = nodes.container()
        self.state.nested_parse(StringList(code), 0, node)
        
        return [node.children[0]]


def setup(app):
    app.add_directive("repeat", RepeatDirective)
    return {"version": "0.1", "parallel_read_safe": True}
