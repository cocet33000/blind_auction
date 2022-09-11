from __future__ import annotations
from injector import inject

from .item_repository import ItemRepository
from ..shared import EventSubscriber
from ..shared import Event
from ..auction import Status


class AuctionEventSubscriber(EventSubscriber):
    @inject
    def __init__(
        self,
        ItemRepositoryImpl: ItemRepository,
    ):
        self.ItemRepository = ItemRepositoryImpl

    def consume(self, auction_event: Event):
        auction_event_type = auction_event.type()  # type: ignore

        if auction_event_type == Status.CLOSED:
            self._consume_closed_event(auction_event)
        elif auction_event_type == Status.OPEN:
            self._consume_open_event(auction_event)

    def _consume_open_event(self, auction_event: Event):
        pass

    def _consume_closed_event(self, auction_event: Event):
        pass
