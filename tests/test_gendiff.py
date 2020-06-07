"""Tests of gendiff."""

import pytest
import os
import json
import yaml

from gendiff import generate_diff, load
from gendiff.cli import run_parse


def test_correct_comparison_of_flat():
    first_file = 'tests/fixtures/t1_before.json'
    second_file = 'tests/fixtures/t1_after.json'
    result_file = 'tests/fixtures/t1_result'
    result_compare = generate_diff(first_file, second_file)
    with open(os.path.abspath(result_file)) as file:
        data_file = file.read()
    assert data_file == result_compare


def test_of_loader_files():
    path_file_json = 'tests/fixtures/t1_before.json'
    path_file_yml = 'tests/fixtures/t1_before.yml'
    path_file_txt = 'tests/fixtures/t1_result'
    data_file = json.load(open(os.path.abspath(path_file_json)))
    assert load(path_file_json) == data_file
    data_file = yaml.safe_load(open(os.path.abspath(path_file_yml)))
    assert load(path_file_yml) == data_file
    data_file = 'Only supported files of type JSON and YAML !'
    assert load(path_file_txt) == data_file


def test_of_parser():
    pass


