from docutils.parsers.rst import Directive
from docutils.statemachine import StringList
from docutils import nodes


class RepeatDirective(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    option_spec = {}

    def run(self):
        text = self.arguments[0]
        
        # Validate that the argument is a valid reference
        valid_refs = ('{numref}', '{ref}', '{prf:ref}')
        if not any(text.startswith(ref) for ref in valid_refs):
            raise self.error(f"repeat directive argument must start with one of: {', '.join(valid_refs)}")
        
        # create dummy code
        code = [f":::{{admonition}} Repeating {text}",
                f":class: repeat",
                f"Content loading...",
                ":::"]
        
        # Parse the code into nodes
        node = nodes.container()
        self.state.nested_parse(StringList(code), 0, node)
        
        return [node.children[0]]


def setup(app):
    app.add_directive("repeat", RepeatDirective)
    return {"version": "0.1", "parallel_read_safe": True}
