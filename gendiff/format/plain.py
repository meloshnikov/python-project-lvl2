"""The module of plain format."""


def render_node(status, key, parent):
    """Renders array nodes.

    Args:
        status (str): Reflects the result of comparison.
        key (str): Name node for rendering.
        parent (str): Parent node for key.

    Returns:
        Result: The formatted string.
    """
    FNODE = "Property '{1}' {2}\n" if parent is None else "Property '{0}.{1}' {2}\n"  # noqa: E501
    if status == 'added':
        result = FNODE.format(
            parent,
            key,
            "was added with value: 'complex value'")
    elif status == 'removed':
        result = FNODE.format(parent, key, 'was removed')
    else:
        result = ''
    return result


def render_branch(parent, status, key, value_after, value_before=None):
    """Renders array branch.

    Args:
        status (str): Reflects the result of comparison.
        key (str): Name branch for rendering.
        parent (str): Parent node for key.
        value_after: value comparable to a key after changes.
        value_before: value comparable to a key before changes.

    Returns:
        Result: The formatted string.
    """
    parent = parent
    if status == 'added':
        result = F_ADDED.format(parent, key, value_after)
    elif status == 'removed':
        result = F_REMOVED.format(parent, key)
    elif status == 'changed':
        result = F_CHANGED.format(parent, key, value_before, value_after)
    else:
        result = ''
    return result


def render_act(diff_dic, parent=None):
    """renders array act.

    Args:
        diff_dic (dict): Dictionary reflecting the difference.
        parent (str): Parent node defined for each node.

    Returns:
        Result: The formatted string.
    """
    result_list = []
    for key, value in sorted(diff_dic.items()):
        status = value[0]
        if isinstance(value[1], dict):
            result_list.append(render_node(status, key, parent))
            result_list.append(render_act(value[1], parent=key))
        elif isinstance(value, tuple):
            result_list.append(
                render_branch(
                    parent,
                    status,
                    key,
                    value[1],
                    value[2]))
        else:
            result_list.append(render_branch(parent, status, key, value))
    return ''.join(result_list)


F_ADDED = "Property '{}.{}' was added with value: '{}'\n"
F_REMOVED = "Property '{}.{}' was removed\n"
F_CHANGED = "Property '{}.{}' was changed. From '{}' to '{}'\n"
