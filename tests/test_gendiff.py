"""Tests of gendiff."""

import pytest
import os

from gendiff import generate_diff


def test_correct_comparison_of_flat_JSON():
    result_compare = generate_diff('tests/fixtures/before.json', 'tests/fixtures/after.json')
    with open(os.path.abspath('tests/fixtures/t1_result')) as file:
        data_file = file.read()
    assert data_file == result_compare
