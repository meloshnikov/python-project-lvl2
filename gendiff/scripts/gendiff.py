# !/usr/bin/env python3

"""The main script."""

from gendiff.engine import parse_args
from gendiff import generate_diff


def main():
    """Run of parser and get compare."""
    args = parse_args()
    diff_result = generate_diff(
        args.first_file,
        args.second_file,
        args.format)
    print(diff_result)


if __name__ == '__main__':
    main()
