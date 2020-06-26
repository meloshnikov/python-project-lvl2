"""The module of json format."""

import json


def render(string):
    return json.dumps(string, indent=2)
