import re

def extract_variables(template_content):
    """
    Finds variables like {{ name }} in template
    """
    pattern = r"\{\{\s*(\w+)\s*\}\}"
    return re.findall(pattern, template_content)

def find_missing_variables(template_vars, context):
    missing = []
    for var in template_vars:
        if var not in context:
            missing.append(var)
    return missing