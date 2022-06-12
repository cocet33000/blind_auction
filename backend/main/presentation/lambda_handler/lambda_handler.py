import os
import json
import logging
from injector import Injector, Module, singleton

from domain.bid import BidRepository
from domain.item import ItemRepository
from infrastructure import BidRepositoryImpl
from infrastructure import ItemRepositoryImpl

from usecase import ItemUseCase
from usecase import BidUseCase

from .handler import handler

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

    return handler(event, context, item_usecase, bid_usecase)
