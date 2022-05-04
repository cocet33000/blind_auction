from get_all_items import get_items
import json


def handler_name(event, context):
    return json.dumps(get_items())
