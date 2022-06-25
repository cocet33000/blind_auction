from __future__ import annotations

import pytest
from mock import Mock
from injector import Injector, Module, singleton

from main.domain.item import ItemRepository
from main.usecase import ItemUseCase

item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.save.return_value = {"is_error": False, "id": "1"}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)


def test_正常系():
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)

    name = "hoge"
    image_src = "http://hoge.jpg"
    description = "hogeです"
    start_price = 10000

    response = item_usecase.register_item(name, image_src, description, start_price)
    assert response["is_error"] == False


def test_価格が数値でない場合はエラー():
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)

    name = "hoge"
    image_src = "http://hoge.jpg"
    description = "hogeです"
    start_price = "hoge"

    with pytest.raises(ValueError):
        item_usecase.register_item(name, image_src, description, start_price)
