"""The module of cascade format."""

from gendiff.constants import ADDED, CHANGED, NOCHANGED, REMOVED, NESTED

BRANCH = "{0}{1} {2}: {3}"
NODE = "{0}{1} {2}: {{ "
END = "{0}  }}"
INDENT = "  "

operators = {
    NESTED: ' ',
    ADDED: '+',
    REMOVED: '-',
    NOCHANGED: ' ',
}


def render_act(diff_dict, depth=1):
    """renders array act.

    Args:
        diff_dict (dict): Dictionary reflecting the difference.
        depth (int): Indent size for rendering.

    Returns:
        Result: The formatted string.
    """
    result_list = []
    indent = INDENT * depth
    for key, value in sorted(diff_dict.items()):
        if isinstance(value, tuple):
            status, values = value
            if isinstance(values, dict):
                result_list.append(NODE.format(indent, operators[status], key))
                result_list.append(render_act(values, depth + 1))
                result_list.append(END.format(indent))
            else:
                result_list.append(render_branch(depth, status, key, values))
        else:
            result_list.append(render_branch(depth, NOCHANGED, key, value))
    return '\n'.join(result_list)


def render_branch(depth, status, key, values):
    result = []
    indent = depth * INDENT
    if status == CHANGED:
        result.append(BRANCH.format(indent, operators[ADDED], key, values[1]))
        result.append(BRANCH.format(indent, operators[REMOVED], key, values[0]))
        result = '\n'.join(result)
    else:
        result = BRANCH.format(indent, operators[status], key, values)
    return result


def render(diff_dict):
    return '{\n' + render_act(diff_dict) + '\n}'
