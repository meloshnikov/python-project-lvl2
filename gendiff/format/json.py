"""The module of json format."""

import json


def render_json(string):
    return json.dumps(string, indent=2)
