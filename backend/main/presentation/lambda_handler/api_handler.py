import json

from main.usecase import ItemUseCase
from main.usecase import BidUseCase

from main.domain.shared import DomainException


def api_handler(
    event: dict, context, item_usecase: ItemUseCase, bid_usecase: BidUseCase
):
    path = event["pathParameters"]["proxy"]
    method = event["requestContext"]["http"]["method"]

    if path == "items":
        if method == "GET":
            try:
                items = item_usecase.get_items()
                return {"statusCode": 200, "body": json.dumps(items)}
            except DomainException as e:
                return {"statusCode": 500, "body": "NG"}

        if method == "POST":
            body = json.loads(event["body"])
            try:
                item_usecase.register_item(
                    name=body.get("name"),
                    image_src=body.get("image_src"),
                    description=body.get("description"),
                    start_price=int(body.get("start_price")),
                )

                return {
                    "statusCode": 200,
                    "body": "OK",
                }
            except DomainException as e:
                return {
                    "statusCode": 500,
                    "body": "NG",
                }

    elif path == "bids":
        if method == "POST":
            body = json.loads(event["body"])

            try:
                bid_usecase.register_bid(
                    user_name=body.get("user_name"),
                    item_id=body.get("item_id"),
                    price=body.get("price"),
                )

                return {
                    "statusCode": 200,
                    "body": "OK",
                }

            except DomainException as e:
                return {
                    "statusCode": 500,
                    "body": "NG",
                }
        elif method == "GET":
            user_name = event["queryStringParameters"].get("user_name")
            try:
                bids_by_user = bid_usecase.get_bids_by_user(user_name=user_name)
                return {
                    "statusCode": 200,
                    "body": json.dumps(bids_by_user),
                }
            except DomainException as e:
                return {
                    "statusCode": 500,
                    "body": "NG",
                }

    else:
        return {"statusCode": 404}
