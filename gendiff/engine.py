"""The main module."""

import json
import os


def load(source_path):
    """Accept the original path and returns the absolute path.

    Args:
        source_path (str): String parameter of original path.

    Returns:
        str: The return of riginal path.
    """
    return json.load(open(os.path.abspath(source_path)))


def process(before, after):
    """Accept two .json files and returns string of differences.

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


NO_CHANGES = '{}: {}'
DELETED = '- {}: {}'
ADDED = '+ {}: {}'
