""" Designer for building a difference ast. """

NESTED = 'nested'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
REMOVED = 'removed'
ADDED = 'added'


def build_ast(before_data, after_data):
    """Compares two objects.

    Args:
        before_data (dict): Original object.
        after_data (dict): Changed object.

    Returns:
        diff_result (dict): Returns a dictionary with comparison results.
    """
    diff_result = {}
    common_items = before_data.keys() & after_data.keys()
    removed_items = before_data.keys() - after_data.keys()
    added_items = after_data.keys() - before_data.keys()
    for key in common_items:
        value_before = before_data[key]
        value_after = after_data[key]
        if isinstance(value_before, dict) and isinstance(value_after, dict):
            diff_result[key] = (NESTED, build_ast(value_before, value_after))
        elif value_before == value_after:
            diff_result[key] = (UNCHANGED, (value_before))
        else:
            diff_result[key] = (CHANGED, (value_before, value_after))
    diff_result.update(
        {
            key: (REMOVED, before_data[key])
            for key in removed_items
        },
    )
    diff_result.update(
        {
            key: (ADDED, after_data[key])
            for key in added_items
        },
    )
    return diff_result
