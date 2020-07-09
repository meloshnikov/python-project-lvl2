# !/usr/bin/env python3

"""The main script."""

from gendiff.engine import parser
from gendiff import generate_diff


def main():
    """Run of parser and get compare."""
    args = parser.parse_args()
    comparison_result = generate_diff(
        args.first_file,
        args.second_file,
        args.format
    )
    print(comparison_result)


if __name__ == '__main__':
    main()
