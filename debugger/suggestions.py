from difflib import get_close_matches

def suggest_variables(missing_vars, context_keys):
    suggestions = {}

    for var in missing_vars:
        matches = get_close_matches(var, context_keys, n=1)
        if matches:
            suggestions[var] = matches[0]
        else:
            suggestions[var] = None

    return suggestions