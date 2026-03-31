from django.template.base import Variable, VariableDoesNotExist
from django.conf import settings
from debugger.suggestions import suggest_variables

original_resolve = Variable.resolve

def custom_resolve(self, context):
    try:
        return original_resolve(self, context)

    except VariableDoesNotExist:
        config = getattr(settings, "TEMPLATE_DEBUGGER", {})

        if not config.get("ENABLED", True):
            return ""

        var_name = self.var
        context_keys = context.flatten().keys()

        suggestions = suggest_variables([var_name], context_keys)
        suggestion = suggestions.get(var_name)

        #  **STRICT MODE**
        if config.get("STRICT_MODE", False):
            raise Exception(
                f"[Template Debugger] Missing variable '{var_name}'. "
                f"Did you mean '{suggestion}'?"
            )

        # FLEXIBLE MODE (default)
        print("\n[Template Debugger]")
        print(f"Missing Variable: {var_name}")
        print(f"Suggestion: {suggestion}")

        return ""

def enable_template_debugger():
    Variable.resolve = custom_resolve