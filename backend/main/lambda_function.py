from get_all_items import get_items
import json


def lambda_handler(event, context):
    return {"statusCode": 200, "body": json.dumps(get_items())}
