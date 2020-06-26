# !/usr/bin/env python3

"""The main script."""

from gendiff import generate_diff
import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
    '-f', '--format',
    default='plain',
    choices=['plain', 'cascade', 'json'],
    help='set format of output')


def main():
    """Run of parser and get compare."""
    args = parser.parse_args()
    diff_result = generate_diff(
        args.first_file,
        args.second_file,
        args.format)
    print(diff_result)


if __name__ == '__main__':
    main()
