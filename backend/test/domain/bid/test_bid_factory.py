from lib2to3.pgen2.token import STAR
import unittest
from mock import Mock

from injector import Injector, Module, singleton

from main.domain.value_object import Price
from main.domain.bid import BidFactory
from main.domain.item import ItemRepository
from main.domain.item import Item

START_PRICE = 1000
item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.getByItemId.return_value = Item(
    id="1",
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


class TestBidFactory(unittest.TestCase):
    def test_開始金額より低い価格はNG(self):
        injector = Injector([DIModule()])
        bid_factory = injector.get(BidFactory)

        BID_PRICE = 999
        with self.assertRaises(ValueError):
            bid_factory.create("hoge", 1, BID_PRICE)

    def test_開始金額と同じ価格はNG(self):
        injector = Injector([DIModule()])
        bid_factory = injector.get(BidFactory)

        BID_PRICE = 1000
        with self.assertRaises(ValueError):
            bid_factory.create("hoge", 1, BID_PRICE)

    def test_開始金額より高い価格はOK(self):
        injector = Injector([DIModule()])
        bid_factory = injector.get(BidFactory)

        BID_PRICE = 1001
        bid = bid_factory.create("hoge", 1, BID_PRICE)
        self.assertEqual(Price(BID_PRICE), bid.price)


if __name__ == "__main__":
    unittest.main()
