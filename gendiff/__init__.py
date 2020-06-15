"""Compares two files and shows the differences."""

from gendiff.engine import load, process, render, warp_act


def generate_diff(first_file, second_file):
    """Accept two files and displays differences.

    Args:
        first_file (str): The first parameter.
        second_file (str): The second parameter.

    """
    before = load(first_file)
    after = load(second_file)
    return warp_act(render(process(before, after)))
