import os
import json
import logging

from get_all_items import get_items
from register_item import register_item
from register_bid import register_bid

logger = logging.getLogger()

if log_level := os.environ.get("LOG_LEVEL"):
    logger.setLevel(log_level)


def lambda_handler(event: dict, context):
    logger.debug(json.dumps(event))

    path = event["pathParameters"]["proxy"]
    method = event["requestContext"]["http"]["method"]

    if path == "items":
        if method == "GET":
            return {"statusCode": 200, "body": json.dumps(get_items())}
        if method == "POST":
            body = json.loads(event["body"])
            response = register_item(
                name=body.get("name"),
                description=body.get("description"),
                start_price=body.get("start_price"),
            )

            if response["is_error"]:
                return {
                    "statusCode": 500,
                    "body": "NG",
                }
            else:
                return {
                    "statusCode": 200,
                    "body": "OK",
                }

    elif path == "bids":
        if method == "POST":
            body = json.loads(event["body"])
            response = register_bid(
                bided_user_id=body.get("bided_user_id"),
                bid_item_id=body.get("bids_item_id"),
                bid_price=body.get("bid_prie"),
            )

            if response["is_error"]:
                return {
                    "statusCode": 500,
                    "body": "NG",
                }
            else:
                return {
                    "statusCode": 200,
                    "body": "OK",
                }
    else:
        return {"statusCode": 404}
