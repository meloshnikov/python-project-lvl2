"""The module of plain format."""

from gendiff.designer import ADDED, CHANGED, UNCHANGED, NESTED, REMOVED

GET_TEMPLATE = {
    ADDED: "'{0}' was added with value: '{1}'",
    REMOVED: "'{0}' was removed",
    CHANGED: "'{0}' was changed. From '{1}' to '{2}'",
}


def render_branch(path, status, value):
    branch_list = ''
    if status == CHANGED:
        branch_list = GET_TEMPLATE[status].format(path, value[0], value[1])
    else:
        value = 'complex value' if isinstance(value, dict) else value
        branch_list = GET_TEMPLATE[status].format(path, value)
    return "Property {}".format(branch_list)


def render_ast(diff_dict, parent=None):
    """renders array act.

    Args:
        diff_dict (dict): Dictionary reflecting the difference.
        parent (str): Contains the path to the root given the parent.

    Returns:
        Result: The formatted string.
    """
    ast_list = []
    for key, (status, values) in sorted(diff_dict.items()):
        if status == NESTED:
            path = key + '.' if parent is None else parent + key + '.'
            ast_list.append(render_ast(values, parent=path))
        elif status != UNCHANGED:
            path = key if parent is None else parent + key
            ast_list.append(render_branch(path, status, values))
    return '\n'.join(ast_list)


def render(diff_dict):
    return render_ast(diff_dict)
