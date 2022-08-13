import os
import json
import logging
from injector import Injector, Module, singleton

from main.domain.bid import BidRepository
from main.domain.item import ItemRepository
from main.domain.auction import AuctionRepository
from main.domain.shared import EventPublisher
from main.domain.item import BidEventSubscriber
from main.infrastructure import BidRepositoryImpl
from main.infrastructure import ItemRepositoryImpl
from main.infrastructure import AuctionRepositoryImpl
from main.infrastructure import EventPublisherImpl

from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase

from .api_handler import api_handler
from .stream_handler import stream_handler

logger = logging.getLogger()

if log_level := os.environ.get("LOG_LEVEL"):
    logger.setLevel(log_level)


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=BidRepositoryImpl)
        binder.bind(ItemRepository, to=ItemRepositoryImpl)
        binder.bind(AuctionRepository, to=AuctionRepositoryImpl)
        binder.bind(EventPublisher, to=EventPublisherImpl)


def lambda_handler(event: dict, context):
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)
    bid_usecase = injector.get(BidUseCase)
    auction_usecase = injector.get(AuctionUseCase)
    bid_event_subscriber = injector.get(BidEventSubscriber)

    logger.debug(json.dumps(event))

    if "pathParameters" in event:
        return api_handler(event, context, item_usecase, bid_usecase, auction_usecase)

    if "Records" in event:
        return stream_handler(
            event, context, item_usecase, bid_usecase, bid_event_subscriber
        )

    return {
        "statusCode": 500,
        "body": "NG",
    }
