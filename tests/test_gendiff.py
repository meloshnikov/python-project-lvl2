"""Tests of gendiff."""

import pytest
import os
import json
import yaml


from gendiff.engine import generate_diff, download


def test_correct_comparison_of_cascade():
    first_file = 'tests/fixtures/t1_before.json'
    second_file = 'tests/fixtures/t1_after.json'
    result_file = 'tests/fixtures/t1_result'
    param = 'cascade'
    with open(os.path.abspath(result_file)) as file:
        data_file = file.read()
    assert data_file == generate_diff(first_file, second_file, param)


def test_comparison_of_complex_plain_json():
    first_file = 'tests/fixtures/t2_before.json'
    second_file = 'tests/fixtures/t2_after.json'
    result_file = 'tests/fixtures/t2_result'
    param = 'cascade'
    with open(os.path.abspath(result_file)) as file:
        data_file = file.read()
    assert data_file == generate_diff(first_file, second_file, param)
    param = 'plain'
    result_file = 'tests/fixtures/t2_result_plain'
    with open(os.path.abspath(result_file)) as file:
        data_file = file.read()
    assert data_file == generate_diff(first_file, second_file, param)
    param = 'json'
    result_file = 'tests/fixtures/t2_result_json'
    with open(os.path.abspath(result_file)) as file:
        data_file = file.read()
    assert data_file == generate_diff(first_file, second_file, param)


def test_of_loader_files():
    path_file_json = 'tests/fixtures/t1_before.json'
    path_file_yml = 'tests/fixtures/t1_before.yml'
    path_file_txt = 'tests/fixtures/t1_result'
    data_file = json.load(open(os.path.abspath(path_file_json)))
    assert download(path_file_json) == data_file
    data_file = yaml.safe_load(open(os.path.abspath(path_file_yml)))
    assert download(path_file_yml) == data_file
    with pytest.raises(SystemExit):
        assert download(path_file_txt) == 'Only supported files of type JSON and YAML !'
