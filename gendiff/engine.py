"""The Gendiff core logic module."""

import argparse
import json
import yaml
import os

from gendiff import format
from gendiff import designer

JSON = 'json'
PLAIN = 'plain'
CASCADE = 'cascade'


def generate_diff(first_file, second_file, format_output):
    """Accept two files and displays differences.

    Args:
        first_file (str): The first parameter.
        second_file (str): The second parameter.
        format(str): The format output result of compare.

    Returns:
        string: The result of comparing two files rendered
        by the module responsible for the format.
        Modules of format:
            format.plain.render(),
            format.cascade.render(),
            format.json.render(),
    """
    try:
        before = load_file(first_file)
        after = load_file(second_file)
        render = get_format(format_output)
        return render(designer.build_ast(before, after))
    except KeyError:
        return 'Only supported files of type json and yaml.'
    except FileNotFoundError:
        return 'File not found'


def load_file(source_path):
    """Deserializes the file into an object.

    Args:
        source_path (str): String parameter of original path.

    Returns:
        obeject: The return a file object type json or yaml.
    """
    METOD_OF_LOAD = {
        'json': json.load,
        'yml': yaml.safe_load,
        'yaml': yaml.safe_load,
    }
    _, extension = os.path.splitext(source_path)
    file_extension = extension[1:].lower()
    return METOD_OF_LOAD[file_extension](open(os.path.abspath(source_path)))


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
    default=PLAIN,
    choices=[PLAIN, CASCADE, JSON],
    help='set format of output')


def get_format(format_output):
    FORMATS = {
        PLAIN: format.plain,
        CASCADE: format.cascade,
        JSON: format.json,
    }
    return FORMATS[format_output]
