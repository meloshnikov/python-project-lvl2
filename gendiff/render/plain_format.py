"""The module of plain format."""

from gendiff.constants import ADDED, CHANGED, NOCHANGED, NESTED, REMOVED


operators = {
    ADDED: "'{0}' was added with value: '{1}'",
    REMOVED: "'{0}' was removed",
    CHANGED: "'{0}' was changed. From '{1}' to '{2}'",
}


def render_branch(path, status, value):
    result = ''
    if status == CHANGED:
        result = operators[status].format(path, value[0], value[1])
    else:
        value = 'complex value' if isinstance(value, dict) else value
        result = operators[status].format(path, value)
    return "Property {}".format(result)


def render_act(diff_dict, parent=None):
    """renders array act.

    Args:
        diff_dict (dict): Dictionary reflecting the difference.
        parent (str): Contains the path to the root given the parent.

    Returns:
        Result: The formatted string.
    """
    result_list = []
    for key, (status, values) in sorted(diff_dict.items()):
        if status == NESTED:
            path = key + '.' if parent is None else parent + key + '.'
            result_list.append(render_act(values, parent=path))
        elif status != NOCHANGED:
            path = key if parent is None else parent + key
            result_list.append(render_branch(path, status, values))
    return '\n'.join(result_list)


def render(diff_dict):
    return render_act(diff_dict)
