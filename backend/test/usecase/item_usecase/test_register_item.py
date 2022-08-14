from __future__ import annotations

import pytest
from mock import Mock
from injector import Injector, Module, singleton

from main.domain.item import ItemRepository
from main.domain.auction import AuctionRepository
from main.usecase import ItemUseCase

item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.save.return_value = {"is_error": False, "id": "1"}

auction_repository_mock = Mock(spec=AuctionRepository)


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)
        binder.bind(AuctionRepository, to=auction_repository_mock)


def test_正常系():
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)

    name = "hoge"
    image_src = "http://hoge.jpg"
    description = "hogeです"
    start_price = 10000
    auction_id = "hoge"

    response = item_usecase.register_item(
        name, image_src, description, start_price, auction_id
    )
    assert not response["is_error"]


def test_価格が数値でない場合はエラー():
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)

    name = "hoge"
    image_src = "http://hoge.jpg"
    description = "hogeです"
    start_price = "hoge"
    auction_id = "hoge"

    with pytest.raises(ValueError):
        item_usecase.register_item(
            name, image_src, description, start_price, auction_id  # type: ignore
        )
