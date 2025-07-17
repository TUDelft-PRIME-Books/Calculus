import re

def replace_text_in_source(app, docname, source):
    """Replace text based on configuration."""
    
    # Get replacements from config
    replacements = getattr(app.config, 'text_replacements', {})
    regex_replacements = getattr(app.config, 'regex_replacements', {})
    
    # Apply simple string replacements
    for old_text, new_text in replacements.items():
        source[0] = source[0].replace(old_text, new_text)
    
    # Apply regex replacements
    for pattern, replacement in regex_replacements.items():
        source[0] = re.sub(pattern, replacement, source[0])

def setup(app):
    # Add configuration values
    app.add_config_value('text_replacements', {}, 'env')
    app.add_config_value('regex_replacements', {}, 'env')
    
    app.connect('source-read', replace_text_in_source)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }