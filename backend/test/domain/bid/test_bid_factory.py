import pytest
from mock import Mock

from injector import Injector, Module, singleton

from main.domain.value_object import Price
from main.domain.bid import BidFactory
from main.domain.item import ItemRepository
from main.domain.item import Item
from main.domain.item import Status

START_PRICE = 1000
item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.getByItemId.return_value = Item.reconstruct(
    id="1",
    status=Status.BEFORE_AUCTION,
    name="fuga",
    image_src="test.png",
    description="fuga",
    start_price=Price(START_PRICE),
    bid_num=0,
)


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)


def test_開始金額より低い価格はNG():
    injector = Injector([DIModule()])
    bid_factory = injector.get(BidFactory)

    BID_PRICE = 999
    with pytest.raises(ValueError):
        bid_factory.create("hoge", "uuid", BID_PRICE)


def test_開始金額と同じ価格はNG():
    injector = Injector([DIModule()])
    bid_factory = injector.get(BidFactory)

    BID_PRICE = 1000
    with pytest.raises(ValueError):
        bid_factory.create("hoge", "uuid", BID_PRICE)


def test_開始金額より高い価格はOK():
    injector = Injector([DIModule()])
    bid_factory = injector.get(BidFactory)

    BID_PRICE = 1001
    bid = bid_factory.create("hoge", "uuid", BID_PRICE)
    assert Price(BID_PRICE) == bid.price
