"""The Gendiff core logic module."""

from gendiff.format import cascade, plain, json
from json import load
from yaml import safe_load
import os
import sys


def generate_diff(first_file, second_file, format):
    """Accept two files and displays differences.

    Args:
        first_file (str): The first parameter.
        second_file (str): The second parameter.
        format(str): The format output result of compare.

    Returns:
        string: The result of comparing two files rendered
        by the module responsible for the format.
        Modules of format:
            plain.render(),
            cascade.render(),
            json.render().
    """
    before = download(first_file)
    after = download(second_file)
    format_render = formatters(format)
    return format_render(process(before, after))


def download(source_path):
    """Deserializes the file into an object.

    Args:
        source_path (str): String parameter of original path.

    Returns:
        obeject: The return a file object type json or yaml.
    """
    _, file_extension = os.path.splitext(source_path)
    if file_extension == '.json':
        return load(open(os.path.abspath(source_path)))
    elif file_extension == '.yml' or file_extension == '.yaml':
        return safe_load(open(os.path.abspath(source_path)))
    else:
        print('Only supported files of type JSON and YAML !')
        sys.exit()


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


def formatters(format):
    formats = {
        'plain': plain.render,
        'cascade': cascade.render,
        'json': json.render
    }
    return formats[format]
