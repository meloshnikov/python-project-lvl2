"""The main module."""

import yaml
import json
import os
import collections


def load(source_path):
    """Takes the original path of the file and deserialize in a file object.

    Args:
        source_path (str): String parameter of original path.

    Returns:
        obeject: The return a file object type json or yaml.
    """
    _, file_extension = os.path.splitext(source_path)
    if file_extension == '.json':
        data_file = json.load(open(os.path.abspath(source_path)))
    elif file_extension == '.yml' or file_extension == '.yaml':
        data_file = yaml.safe_load(open(os.path.abspath(source_path)))
    else:
        data_file = 'Only supported files of type JSON and YAML !'
    return data_file



def process(before_data, after_data):
    diff_result = {}
    common_items = before_data.keys() & after_data.keys()
    removed_items = before_data.keys() - after_data.keys()
    added_items = after_data.keys() - before_data.keys()
    for key in common_items:
        value_before = before_data[key]
        value_after = after_data[key]
        if isinstance(value_before, dict) and isinstance(value_after, dict):
            diff_result[key] = ('node', process(value_before, value_after))
        elif value_before == value_after:
            diff_result[key] = ('nochanged', value_before, None)
        else:
            diff_result[key] = ('changed', value_after, value_before)
    for key in removed_items:
        diff_result[key] = ('removed', before_data[key], None)
    for key in added_items:
        diff_result[key] = ('added', after_data[key], None)
    return diff_result


def render_node(status, key, depth):
    depth = depth * '  '
    if status == 'node':
        result = NODE.format(depth, ' ', key)
    elif status == 'added':
        result = NODE.format(depth, '+', key)
    elif status == 'removed':
        result = NODE.format(depth, '-', key)
    return result
    

def render_branch(depth, status, key, value_after, value_before=None):
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



def render(diff_dic, depth=1):
    result_list = []
    count = 0
    for key, value in sorted(diff_dic.items()):
        status = value[0]
        if isinstance(value[1], dict):
            result_list.append(render_node(status, key, depth))
            result_list.append(render(value[1], depth + 1))
            result_list.append(END.format((depth * '   ')))
        elif isinstance(value, tuple):
            result_list.append(render_branch(depth, status, key, value[1], value[2]))
        else:
            result_list.append(render_branch(depth, status, key, value))
    return ''.join(result_list)


def warp_act(string):
    string = '{\n' + string + '}'
    return string 

BRANCH = "{}{} {}: {}\n"
NODE = "{}{} {}: {{ \n"
END = "{}}}\n"
