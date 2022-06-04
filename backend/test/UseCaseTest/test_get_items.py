from __future__ import annotations

import unittest
from pathlib import Path
import sys
from injector import Injector, Module, singleton

sys.path.append(str(Path(__file__).parent.parent.parent / "main"))

from Infrastructure import ItemRepository
import DomainModel
from UseCase import ItemUseCase


item1 = DomainModel.Item(
    id="1",
    name="hoge",
    image_src="test.png",
    description="hoge",
    start_price=100,
    bid_num=0,
)
item2 = DomainModel.Item(
    id="2",
    name="fuga",
    image_src="test.png",
    description="fuga",
    start_price=100,
    bid_num=0,
)


class ItemRepositoryMock(ItemRepository):
    @staticmethod
    def save(item: DomainModel.Item) -> dict:
        return {"is_error": False, "id": item.id}

    @staticmethod
    def getByItemId(item_id):
        item = DomainModel.Item(
            id=item_id,
            name="hoge",
            image_src="test.png",
            description="fuga",
            start_price=100,
            bid_num=0,
        )
        return item

    @staticmethod
    def getAll() -> list[DomainModel.Item]:
        return [item1, item2]

    @staticmethod
    def deleteByItemId(item_id):
        return "OK"


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=ItemRepositoryMock)


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
