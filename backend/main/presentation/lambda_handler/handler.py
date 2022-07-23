import os
import json
import logging
from injector import Injector, Module, singleton

from main.domain.bid import BidRepository
from main.domain.bid import BidEvent
from main.domain.item import ItemRepository
from main.domain.shared import EventPublisher
from main.domain.item import BidEventSubscriber
from main.infrastructure import BidRepositoryImpl
from main.infrastructure import ItemRepositoryImpl
from main.infrastructure import EventPublisherImpl

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
        binder.bind(EventPublisher, to=EventPublisherImpl)


def lambda_handler(event: dict, context):
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)
    bid_usecase = injector.get(BidUseCase)
    bid_event_subscriber = injector.get(BidEventSubscriber)

    logger.debug(json.dumps(event))

    if "pathParameters" in event:
        return api_handler(event, context, item_usecase, bid_usecase)

    if "Records" in event:
        return stream_handler(
            event, context, item_usecase, bid_usecase, bid_event_subscriber
        )

    return {
        "statusCode": 500,
        "body": "NG",
    }


def api_handler(
    event: dict, context, item_usecase: ItemUseCase, bid_usecase: BidUseCase
):
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


def stream_handler(
    event: dict,
    context,
    item_usecase: ItemUseCase,
    bid_usecase: BidUseCase,
    bid_event_subscriber: BidEventSubscriber,
):
    logger.debug(json.dumps(event))

    try:
        event_name, event_details = parse_event(event)
    except Exception as e:
        logger.error(e)
        return {"statusCode": 500, "body": "NG"}

    try:
        if event_name == "BID":
            bid_event = BidEvent.reconstruct(event_details)
            logger.debug(json.dumps(bid_event))
            bid_event_subscriber.consume(bid_event)
        return {"statusCode": 200, "body": "OK", "eventName": event_name}
    except Exception as e:
        logger.error(e)
        return {"statusCode": 200, "body": "OK", "eventName": event_name}


def parse_event(event: dict):
    event_name = event["Records"][0]["dynamodb"]["NewImage"]["name"]["S"]
    event_details = event["Records"][0]["dynamodb"]["NewImage"]["details"]["M"]
    return event_name, event_details
