"""Compares two files and shows the differences."""

from gendiff.engine import download, process
from gendiff.format import cascade, json, plain


def generate_diff(first_file, second_file, parameter):
    """Accept two files and displays differences.

    Args:
        first_file (str): The first parameter.
        second_file (str): The second parameter.
        parameter(str): The format output result of compare.

    Returns:
        string: The result comparing two files.
    """
    before = download(first_file)
    after = download(second_file)
    if parameter == 'plain':
        return plain.render_act(process(before, after))
    elif parameter == 'cascade':
        return cascade.warp_act(cascade.render_act(process(before, after)))
    elif parameter == 'json':
        return json.render_json(process(before, after))
