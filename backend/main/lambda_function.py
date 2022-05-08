import os
import json
import logging

from UseCase import get_items
from UseCase import register_item
from UseCase import register_bid
from UseCase import get_bids_by_user

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
                image_src=body.get("image_src"),
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
                user_name=body.get("user_name"),
                item_id=body.get("item_id"),
                price=body.get("price"),
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
        elif method == "GET":
            user_name = event["queryStringParameters"].get("user_name")
            return {
                "statusCode": 200,
                "body": json.dumps(get_bids_by_user(user_name=user_name)),
            }

    else:
        return {"statusCode": 404}
