"""Compares two files and shows the differences."""

from gendiff.engine import load, process
from gendiff.format import plain
from gendiff.format import human
#import os


def generate_diff(first_file, second_file, parameter):
    """Accept two files and displays differences.

    Args:
        first_file (str): The first parameter.
        second_file (str): The second parameter.

    """
    before = load(first_file)
    after = load(second_file)
    if parameter == 'plain':
        return plain.render_act(process(before, after))
    elif parameter == 'human':
        return human.warp_act(human.render_act(process(before, after)))
    #f = open(os.path.abspath('test'), 'w')
    #f.write(render_act(process(before, after)))
    #return render_act(process(before, after))
