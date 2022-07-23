from __future__ import annotations

from mock import Mock

from injector import Injector, Module, singleton

from main.domain.item import ItemRepository
from main.domain.bid import BidEvent
from main.domain.item.bid_event_subscriber import BidEventSubscriber

item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.bidNumIncrement.return_value = {"is_error": False}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)


def test_正常系():
    injector = Injector([DIModule()])
    bid_event_subscriber = injector.get(BidEventSubscriber)

    bid_event = BidEvent(user_name="hoge", item_id="1", price=100)
    res = bid_event_subscriber.consume(bid_event)

    assert res.get("is_error") is False
