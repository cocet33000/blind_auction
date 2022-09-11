from __future__ import annotations
from injector import inject

from .item_repository import ItemRepository
from ..shared import EventSubscriber
from ..shared import Event


class BidEventSubscriber(EventSubscriber):
    @inject
    def __init__(
        self,
        ItemRepositoryImpl: ItemRepository,
    ):
        self.ItemRepository = ItemRepositoryImpl

    def consume(self, bid_event: Event):
        item_id = bid_event.item_id()  # type: ignore
        return self.ItemRepository.bidNumIncrement(item_id)  # type: ignore
