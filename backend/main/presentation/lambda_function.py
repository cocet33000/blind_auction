import os
import json
import logging
from injector import Injector, Module, singleton

from main.domain.bid import BidRepository
from main.domain.item import ItemRepository
from main.infrastructure import BidRepositoryImpl
from main.infrastructure import ItemRepositoryImpl

from main.usecase import ItemUseCase
from main.usecase import BidUseCase

logger = logging.getLogger()

if log_level := os.environ.get("LOG_LEVEL"):
    logger.setLevel(log_level)


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=BidRepositoryImpl)
        binder.bind(ItemRepository, to=ItemRepositoryImpl)


def lambda_handler(event: dict, context):
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)
    bid_usecase = injector.get(BidUseCase)

    logger.debug(json.dumps(event))

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
