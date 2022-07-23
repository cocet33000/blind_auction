from __future__ import annotations
from injector import inject

from ..bid import BidEvent
from ..shared import EventSubscriber
from . import ItemRepository


class BidEventSubscriber(EventSubscriber):
    @inject
    def __init__(
        self,
        ItemRepositoryImpl: ItemRepository,
    ):
        self.ItemRepository = ItemRepositoryImpl

    def consume(self, bid_event: BidEvent):
        item_id = bid_event.item_id()
        return self.ItemRepository.bidNumIncrement(item_id)
