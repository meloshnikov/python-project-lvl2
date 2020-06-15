"""The module of plain format."""



def render_node(status, key, parent):
    FNODE = "Property '{1}' {2}\n" if parent is None else "Property '{0}.{1}' {2}\n"
    if status == 'added':
        result = FNODE.format(parent, key, "was added with value: 'complex value'")
    elif status == 'removed':
        result = FNODE.format(parent, key, 'was removed')
    else:
        result = ''
    return result
    

def render_branch(parent, status, key, value_after, value_before=None):
    parent = parent
    if status == 'added':
        result = "Property '{}.{}' was added with value: '{}'\n".format(parent, key, value_after)
    elif status == 'removed':
        result = "Property '{}.{}' was removed\n".format(parent, key)
    elif status == 'changed':
        result = "Property '{}.{}' was changed. From '{}' to '{}'\n".format(parent, key, value_before, value_after)
    else:
        result = ''
    return result



def render_act(diff_dic, parent=None):
    result_list = []
    count = 0
    for key, value in sorted(diff_dic.items()):
        status = value[0]
        if isinstance(value[1], dict):
            result_list.append(render_node(status, key, parent))
            result_list.append(render_act(value[1], parent=key))
        elif isinstance(value, tuple):
            result_list.append(render_branch(parent, status, key, value[1], value[2]))
        else:
            result_list.append(render_branch(parent, status, key, value))
    return ''.join(result_list)
