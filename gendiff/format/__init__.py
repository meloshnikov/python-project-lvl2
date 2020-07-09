"""This is module of formats."""

from gendiff.format.json import render as json
from gendiff.format.plain import render as plain
from gendiff.format.cascade import render as cascade

__all__ = ['json', 'plain', 'cascade']
