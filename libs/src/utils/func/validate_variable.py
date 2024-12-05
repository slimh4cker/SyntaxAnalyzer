def detect_uninitialized_variables(expr, variables):
    """
    hasattr func usage -> hasattr(obj, "attribute_name")
    04/12/2024
    """
    uninitialized_variables = []
    if hasattr(expr, 'ID'):
        variable_name = expr.ID().getText()
        if variable_name not in variables:
            uninitialized_variables.append(variable_name)
    elif hasattr(expr, 'children'):
        for child in expr.children:
            uninitialized_variables.extend(detect_uninitialized_variables(child, variables))
    return uninitialized_variables
