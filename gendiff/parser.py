"""The main module."""

import argparse


def func():
    """Init of parser objects."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='first_file')
    parser.add_argument('second_file', type=str, help='second_file')
    args = parser.parse_args()
    print(args.first_file)  # noqa: WPS421
