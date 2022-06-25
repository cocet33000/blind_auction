from __future__ import annotations

from mock import Mock
from injector import Injector, Module, singleton

from main.domain.item import ItemRepository
from main.domain.item import Item
from main.domain.value_object import Price

from main.usecase import ItemUseCase

item1 = Item.reconstruct(
    id="1",
    name="hoge",
    image_src="test.png",
    description="hoge",
    start_price=Price(100),
    bid_num=0,
)
item2 = Item.reconstruct(
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


def test_get_items():
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)
    response = item_usecase.get_items()

    assert response["items"][0]["id"] == item1.id
    assert response["items"][0]["name"] == item1.name
    assert response["items"][0]["image_src"] == item1.image_src
    assert response["items"][0]["description"] == item1.description
    assert response["items"][0]["start_price"] == item1.start_price
    assert response["items"][0]["bid_num"] == item1.bid_num

    assert response["items"][1]["id"] == item2.id
    assert response["items"][1]["name"] == item2.name
    assert response["items"][1]["image_src"] == item2.image_src
    assert response["items"][1]["description"] == item2.description
    assert response["items"][1]["start_price"] == item2.start_price
    assert response["items"][1]["bid_num"] == item2.bid_num
