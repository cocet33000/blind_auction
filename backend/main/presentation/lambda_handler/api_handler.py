import json
import logging
from datetime import datetime

from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase
from main.usecase import QueryUseCase

from main.domain.shared import DomainException

from ..openapi_server.models.auctions_post_request import AuctionsPostRequest

from .serialize import (
    bids_history_serialize,
    commands_auctions_response_serialize,
    home_get_response_serialize,
)
from .serialize import auctions_get_reonse_seririalize


def bad_request_response(e):
    return {
        "statusCode": 400,
        "body": json.dumps(e.message()),
        "headers": {"content-type": "application/json;charset=UTF-8"},
    }


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
                logging.exception("")
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
                    auction_id=body.get("auction_id"),
                )

                return {
                    "statusCode": 200,
                    "body": "OK",
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }
            except DomainException as e:
                logging.exception("")
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
                logging.exception("")
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
                logging.exception("")
                return {
                    "statusCode": 500,
                    "body": json.dumps({"message": e.message()}),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }

    elif path == "auctions":
        if method == "GET":
            try:
                auctions = auction_usecase.get_auctions_all()

                return {
                    "statusCode": 200,
                    "body": json.dumps(
                        auctions_get_reonse_seririalize(auctions),
                    ),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }
            except DomainException as e:
                logging.exception("Error in stream event handling")
                return {
                    "statusCode": 500,
                    "body": json.dumps({"message": e.message()}),
                }
        elif method == "POST":
            body = json.loads(event["body"])

            try:
                auctions_post_request = AuctionsPostRequest.from_dict(body)
            except Exception as e:
                logging.exception("")
                return bad_request_response(e)

            try:
                auction_usecase.register_auction(
                    name=auctions_post_request.name,  # type: ignore
                    start_datetime=datetime.strptime(
                        auctions_post_request.start_datetime,  # type: ignore
                        "%Y/%m/%d %H:%M",
                    ),
                    end_datetime=datetime.strptime(
                        auctions_post_request.end_datetime,  # type: ignore
                        "%Y/%m/%d %H:%M",
                    ),
                )

                return {
                    "statusCode": 200,
                    "body": "OK",
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }

            except DomainException as e:
                logging.exception("")
                return {
                    "statusCode": 500,
                    "body": json.dumps({"message": e.message()}),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }

    if path == "home":
        if method == "GET":
            try:
                auction = auction_usecase.get_opening_auction()
                items = item_usecase.get_items_by_auction_id(auction.id())

                return {
                    "statusCode": 200,
                    "body": json.dumps(home_get_response_serialize(auction, items)),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }
            except DomainException as e:
                logging.exception("")
                return {
                    "statusCode": 500,
                    "body": json.dumps(({"message": e.message()})),
                    "headers": {"content-type": "application/json;charset=UTF-8"},
                }

    elif path == "commands/auctions":
        if method == "POST":
            auction_events = auction_usecase.switch_auction()
            return {
                "statusCode": 200,
                "body": json.dumps(
                    commands_auctions_response_serialize(auction_events)
                ),
                "headers": {"content-type": "application/json;charset=UTF-8"},
            }

    else:
        return {"statusCode": 404}
