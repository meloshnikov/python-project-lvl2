"""Tests of gendiff."""

from unittest import mock
import argparse
import pathlib
import pytest
import os

from gendiff import engine

TESTDIR = pathlib.Path(__file__).parent.absolute()
FIXDIR = TESTDIR / 'fixtures'


@pytest.mark.parametrize(
    'file1,file2,output_format,output_file', [
        ('flat_input_1.json', 'flat_input_2.json', 'cascade', 'flat_cascade_output'),
        ('flat_input_1.yml', 'flat_input_2.yml', 'cascade', 'flat_cascade_output'),
        ('nested_input_1.json', 'nested_input_2.json', 'cascade', 'nested_cascade_output'),
        ('nested_input_1.yml', 'nested_input_2.yml', 'json', 'nested_json_output.json'),
        ('nested_input_1.json', 'nested_input_2.json', 'plain', 'nested_plain_output.txt'),
    ],
)
def test_correct_comparison(file1, file2, output_format, output_file):
    file_path = FIXDIR / output_file
    with open(os.path.abspath(file_path)) as file:
        data_file = file.read()
    assert engine.generate_diff(
        FIXDIR / file1,
        FIXDIR / file2,
        output_format,
    ) == data_file


@pytest.mark.parametrize(
    'file1,file2,output_format,exception', [
        ('flat_input_1.txt', 'flat_input_2.json', 'plain', 'Only supported files of type json and yaml.'),
        ('nonexistent_file.json', 'flat_input_2.yml', 'plain', 'File not found'),
    ],
)
def test_exception(file1, file2, output_format, exception):
    assert engine.generate_diff(
        FIXDIR / file1,
        FIXDIR / file2,
        output_format,
    ) == exception


@mock.patch(
    'argparse.ArgumentParser.parse_args',
    return_value=argparse.Namespace(
        first_file='./test.json',
        second_file='./test.json',
        format='plain',
    )
)
def test_parser(mock_args):
    args = engine.parser.parse_args()
    assert args.first_file == './test.json'
    assert args.second_file == './test.json'
    assert args.format == 'plain'
