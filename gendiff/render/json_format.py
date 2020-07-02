"""The module of json format."""

import json


def render(string):
    return json.dumps(string, sort_keys=True, indent=2)
