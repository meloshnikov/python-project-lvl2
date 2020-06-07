# !/usr/bin/env python3

"""The main script."""

import argparse

from gendiff import generate_diff


def main():
    """Init of parser objects."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    comparison_result = generate_diff(args.first_file, args.second_file)
    print(comparison_result)

if __name__ == '__main__':
    main()
