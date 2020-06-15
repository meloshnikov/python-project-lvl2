"""The cli module."""


import argparse

from gendiff import generate_diff


def run_parse():
    """Init of parser objects."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output',
                        default='plain', choices=['plain', 'human'])
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))
