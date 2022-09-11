from __future__ import annotations

from mock import Mock

from injector import Injector, Module, singleton

from main.domain.item import ItemRepository
from main.domain.auction import Status
from main.domain.auction import AuctionEvent
from main.domain.item.auction_event_subscriber import AuctionEventSubscriber

item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.bidNumIncrement.return_value = {"is_error": False}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)


def test_正常系_CLOSED():
    injector = Injector([DIModule()])
    auction_event_subscriber = injector.get(AuctionEventSubscriber)

    AUCTION_ID = "hoge"
    AUCTION_NAME = "fuga"
    TYPE = Status.CLOSED

    auction_event = AuctionEvent(
        auction_id=AUCTION_ID, auction_name=AUCTION_NAME, type=TYPE
    )

    auction_event_subscriber.consume(auction_event)


def test_正常系_OPEN():
    injector = Injector([DIModule()])
    auction_event_subscriber = injector.get(AuctionEventSubscriber)

    AUCTION_ID = "hoge"
    AUCTION_NAME = "fuga"
    TYPE = Status.OPEN

    auction_event = AuctionEvent(
        auction_id=AUCTION_ID, auction_name=AUCTION_NAME, type=TYPE
    )

    auction_event_subscriber.consume(auction_event)
