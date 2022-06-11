from __future__ import annotations

import unittest
from mock import Mock
from injector import Injector, Module, singleton

from domain.item.item_repository import ItemRepository
from usecase.item_usecase import ItemUseCase
from domain.item.item import Item
from domain.value_object.price import Price

item1 = Item(
    id="1",
    name="hoge",
    image_src="test.png",
    description="hoge",
    start_price=Price(100),
    bid_num=0,
)
item2 = Item(
    id="2",
    name="fuga",
    image_src="test.png",
    description="fuga",
    start_price=Price(100),
    bid_num=0,
)

item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.getAll.return_value = [item1, item2]


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)


class TestGetItems(unittest.TestCase):
    def test_get_items(self):
        injector = Injector([DIModule()])
        item_usecase = injector.get(ItemUseCase)
        response = item_usecase.get_items()

        self.assertEqual(response["items"][0]["id"], item1.id)
        self.assertEqual(response["items"][0]["name"], item1.name)
        self.assertEqual(response["items"][0]["image_src"], item1.image_src)
        self.assertEqual(response["items"][0]["description"], item1.description)
        self.assertEqual(response["items"][0]["start_price"], item1.start_price)
        self.assertEqual(response["items"][0]["bid_num"], item1.bid_num)

        self.assertEqual(response["items"][1]["id"], item2.id)
        self.assertEqual(response["items"][1]["name"], item2.name)
        self.assertEqual(response["items"][1]["image_src"], item2.image_src)
        self.assertEqual(response["items"][1]["description"], item2.description)
        self.assertEqual(response["items"][1]["start_price"], item2.start_price)
        self.assertEqual(response["items"][1]["bid_num"], item2.bid_num)
