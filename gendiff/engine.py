"""The main module."""


import json
import os
import yaml


def download(source_path):
    """Deserializes the file into an object.

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
    """Compares two objects.

    Args:
        before_data (dict): Original object.
        after_data (dict): Changed object.

    Returns:
        diff_result (dict): Returns a dictionary with comparison results.
    """
    diff_result = {}
    common_items = sorted(before_data.keys() & after_data.keys())
    removed_items = sorted(before_data.keys() - after_data.keys())
    added_items = sorted(after_data.keys() - before_data.keys())
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
