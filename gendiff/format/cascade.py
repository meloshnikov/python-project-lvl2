"""The module of cascade format."""

from gendiff.designer import ADDED, CHANGED, UNCHANGED, NESTED, REMOVED

BRANCH = "{0}{1} {2}: {3}"
NODE = "{0}{1} {2}: {{ "
END = "{0}  }}"
INDENT = "  "

GET_SYMBOLL = {
    NESTED: ' ',
    ADDED: '+',
    REMOVED: '-',
    UNCHANGED: ' ',
}


def render_ast(diff_dict, depth=1):
    """renders array act.

    Args:
        diff_dict (dict): Dictionary reflecting the difference.
        depth (int): Indent size for rendering.

    Returns:
        Result: The formatted string.
    """
    ast_list = []
    indent = INDENT * depth
    for key, value in sorted(diff_dict.items()):
        if isinstance(value, tuple):
            status, values = value
            if isinstance(values, dict):
                ast_list.append(NODE.format(indent, GET_SYMBOLL[status], key))
                ast_list.append(render_ast(values, depth + 1))
                ast_list.append(END.format(indent))
            else:
                ast_list.append(render_branch(depth, status, key, values))
        else:
            ast_list.append(render_branch(depth, UNCHANGED, key, value))
    return '\n'.join(ast_list)


def render_branch(depth, status, key, values):
    branch_list = []
    indent = depth * INDENT
    if status == CHANGED:
        branch_list.append(
            BRANCH.format(indent, GET_SYMBOLL[ADDED], key, values[1])
        )
        branch_list.append(
            BRANCH.format(indent, GET_SYMBOLL[REMOVED], key, values[0])
        )
        branch_list = '\n'.join(branch_list)
    else:
        branch_list = BRANCH.format(indent, GET_SYMBOLL[status], key, values)
    return branch_list


def render(diff_dict):
    return '{\n' + render_ast(diff_dict) + '\n}'
