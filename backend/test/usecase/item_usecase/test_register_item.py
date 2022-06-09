from __future__ import annotations

import unittest
from mock import Mock
from injector import Injector, Module, singleton

from main.domain.item.item_repository import ItemRepository
from main.usecase.item_usecase import ItemUseCase
from main.domain.item.item import Item
from main.domain.value_object.price import Price

item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.save.return_value = {"is_error": False, "id": "1"}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)


class TestRegisterItem(unittest.TestCase):
    def test_正常系(self):
        injector = Injector([DIModule()])
        item_usecase = injector.get(ItemUseCase)

        name = "hoge"
        image_src = "http://hoge.jpg"
        description = "hogeです"
        start_price = 10000

        response = item_usecase.register_item(name, image_src, description, start_price)
        self.assertEqual(response["is_error"], False)

    def test_価格が数値でない場合はエラー(self):
        injector = Injector([DIModule()])
        item_usecase = injector.get(ItemUseCase)

        name = "hoge"
        image_src = "http://hoge.jpg"
        description = "hogeです"
        start_price = "hoge"

        with self.assertRaises(ValueError):
            item_usecase.register_item(name, image_src, description, start_price)
