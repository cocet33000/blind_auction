import json

from main.usecase import ItemUseCase
from main.usecase import BidUseCase


def handler(event: dict, context, item_usecase: ItemUseCase, bid_usecase: BidUseCase):
    path = event["pathParameters"]["proxy"]
    method = event["requestContext"]["http"]["method"]

    if path == "items":
        if method == "GET":
            # ここで詰め替える
            return {"statusCode": 200, "body": json.dumps(item_usecase.get_items())}
        if method == "POST":
            body = json.loads(event["body"])
            response = item_usecase.register_item(
                name=body.get("name"),
                image_src=body.get("image_src"),
                description=body.get("description"),
                start_price=int(body.get("start_price")),
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
            response = bid_usecase.register_bid(
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
                "body": json.dumps(bid_usecase.get_bids_by_user(user_name=user_name)),
            }

    else:
        return {"statusCode": 404}
