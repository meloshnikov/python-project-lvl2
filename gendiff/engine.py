"""The main module."""

import yaml
import json
import os


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


def process(before, after):
    """Takes two objects and returns string of differences.

    Args:
        before (dict): Source file for comparison.
        after (dict): Modified file for comparison.

    Returns:
        str: The returns of string of differences.
    """
    added_key = set(after) - set(before)
    comparison_result = ['{\n']
    for key, value in before.items():
        if after.get(key, None) == value:
            comparison_result.append(NO_CHANGES.format(key, value))
            comparison_result.append('\n')
        elif after.get(key, None) is None:
            comparison_result.append(DELETED.format(key, value))
            comparison_result.append('\n')
        else:
            comparison_result.append(ADDED.format(key, after.get(key, None)))
            comparison_result.append('\n')
            comparison_result.append(DELETED.format(key, value))
            comparison_result.append('\n')
    for key in added_key:
        comparison_result.append(ADDED.format(key, after.get(key, None)))
        comparison_result.append('\n')
    comparison_result.append('}')
    return ''.join(comparison_result)


NO_CHANGES = '  {}: {}'
DELETED = '  - {}: {}'
ADDED = '  + {}: {}'
