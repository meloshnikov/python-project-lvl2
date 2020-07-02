"""The Gendiff core logic module."""

from gendiff.render import cascade_format, plain_format, json_format
from gendiff.constants import ADDED, CHANGED, NOCHANGED, NESTED, REMOVED
import argparse
import json
import yaml
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
            plain_format.render(),
            cascade_format.render(),
            json_format.render().
    """
    before = load_file(first_file)
    after = load_file(second_file)
    render = _call_render(format)
    return render(process(before, after))


def load_file(source_path):
    """Deserializes the file into an object.

    Args:
        source_path (str): String parameter of original path.

    Returns:
        obeject: The return a file object type json or yaml.
    """
    metod_of_load = {
        'json': json.load,
        'yml': yaml.safe_load,
        'yaml': yaml.safe_load,
    }
    try:
        file_extension = os.path.splitext(source_path)[1][1:].lower()
        return metod_of_load[file_extension](open(os.path.abspath(source_path)))
    except KeyError:
        print('Oops! Only supported files of type json and yaml.')
        sys.exit()
    except FileNotFoundError:
        print('No such file or directory:', os.path.abspath(source_path))
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
    common_items = before_data.keys() & after_data.keys()
    removed_items = before_data.keys() - after_data.keys()
    added_items = after_data.keys() - before_data.keys()
    for key in common_items:
        value_before = before_data[key]
        value_after = after_data[key]
        if isinstance(value_before, dict) and isinstance(value_after, dict):
            diff_result[key] = (NESTED, process(value_before, value_after))
        elif value_before == value_after:
            diff_result[key] = (NOCHANGED, (value_before))
        else:
            diff_result[key] = (CHANGED, (value_before, value_after))
    diff_result.update(
        {
            key: (REMOVED, before_data[key])
            for key in removed_items
        },
    )
    diff_result.update(
        {
            key: (ADDED, after_data[key])
            for key in added_items
        },
    )
    return diff_result


def parse_args():
    """Parse arguments.

    Automatically generate help and usage messages.

    Returns:
        arguments (str): Get from the command line,
        convert to the appropriate type.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        default='plain',
        choices=['plain', 'cascade', 'json'],
        help='set format of output')
    return parser.parse_args()


def _call_render(format):
    formats = {
        'plain': plain_format.render,
        'cascade': cascade_format.render,
        'json': json_format.render,
    }
    return formats[format]
