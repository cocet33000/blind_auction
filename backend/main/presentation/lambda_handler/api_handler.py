import json

from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase
from main.usecase import QueryUseCase

from main.domain.shared import DomainException

from .serialize import bids_history_serialize


def api_handler(
    event: dict,
    context,
    item_usecase: ItemUseCase,
    bid_usecase: BidUseCase,
    auction_usecase: AuctionUseCase,
    query_usecase: QueryUseCase,
):
    path = event["pathParameters"]["proxy"]
    method = event["requestContext"]["http"]["method"]

    if path == "items":
        if method == "GET":
            try:
                items = item_usecase.get_items()
                return {
                    "statusCode": 200,
                    "body": json.dumps(items),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }
            except DomainException as e:
                return {
                    "statusCode": 500,
                    "body": json.dumps(({"message": e.message()})),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }

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
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }
            except DomainException as e:
                return {
                    "statusCode": 500,
                    "body": json.dumps({"message": e.message()}),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
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
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }

            except DomainException as e:
                return {
                    "statusCode": 500,
                    "body": json.dumps({"message": e.message()}),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }
        elif method == "GET":
            user_name = event["queryStringParameters"].get("user_name")
            try:
                bids_by_user = query_usecase.get_bid_history(user_name=user_name)

                return {
                    "statusCode": 200,
                    "body": json.dumps(bids_history_serialize(bids_by_user)),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }
            except DomainException as e:
                return {
                    "statusCode": 500,
                    "body": json.dumps({"message": e.message()}),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }

    elif path == "auctions":
        if method == "GET":
            try:
                auctions = [
                    auction.to_dict() for auction in auction_usecase.get_auctions_all()
                ]
                return {
                    "statusCode": 200,
                    "body": json.dumps({"has_next:": False, "auctions": auctions}),
                }
            except DomainException as e:
                return {
                    "statusCode": 500,
                    "body": json.dumps({"message": e.message()}),
                }
    else:
        return {"statusCode": 404}
