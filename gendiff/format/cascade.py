"""The module of cascade format."""


def render_node(status, key, depth):
    """Renders array nodes.

    Args:
        status (str): Reflects the result of comparison.
        key (str): Name node for rendering.
        depth (str): Indent size.

    Returns:
        Result: The formatted string.
    """
    depth = depth * '  '
    if status == 'added':
        result = NODE.format(depth, '+', key)
    elif status == 'removed':
        result = NODE.format(depth, '-', key)
    else:
        result = NODE.format(depth, ' ', key)
    return result


def render_branch(depth, status, key, value_after, value_before=None):
    """Renders array branch.

    Args:
        status (str): Reflects the result of comparison.
        key (str): Name branch for rendering.
        depth (str): Indent size.
        value_after: value comparable to a key after changes.
        value_before: value comparable to a key before changes.

    Returns:
        Result: The formatted string.
    """
    depth = depth * '  '
    if status == 'added':
        result = BRANCH.format(depth, '+', key, value_after)
    elif status == 'removed':
        result = BRANCH.format(depth, '-', key, value_after)
    elif status == 'changed':
        result = BRANCH.format(depth, '+', key, value_after)
        result += BRANCH.format(depth, '-', key, value_before)
    else:
        result = BRANCH.format(depth, ' ', key, value_after)
    return result


def render_act(diff_dic, depth=1):
    """renders array act.

    Args:
        diff_dic (dict): Dictionary reflecting the difference.
        depth (int): Indent size for rendering.

    Returns:
        Result: The formatted string.
    """
    result_list = []
    for key, value in sorted(diff_dic.items()):
        status = value[0]
        if isinstance(value[1], dict):
            result_list.append(render_node(status, key, depth))
            result_list.append(render_act(value[1], depth + 1))
            result_list.append(END.format((depth * '   ')))
        elif isinstance(value, tuple):
            result_list.append(
                render_branch(
                    depth,
                    status,
                    key,
                    value[1],
                    value[2]))
        else:
            result_list.append(render_branch(depth, status, key, value))
    return ''.join(result_list)


def warp_act(string):
    string = '{\n' + string + '}'
    return string


BRANCH = "{}{} {}: {}\n"
NODE = "{}{} {}: {{ \n"
END = "{}}}\n"
