from __future__ import annotations
import pytest

from main.presentation.lambda_handler import handler

from mock import Mock

from main.usecase import ItemUseCase
from main.usecase import BidUseCase

from main.domain.item import Item
from main.domain.value_object import Price

items = [
    Item(
        id="1",
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
    )
]

item_usecase_mock = Mock(spec=ItemUseCase)
item_usecase_mock.get_items.return_value = {"items": [item.to_dict() for item in items]}
bid_usecase_mock = Mock(spec=BidUseCase)


def test_商品一覧を取得():
    # TODO: リクエスト内容を別ファイルで用意する
    event = {
        "pathParameters": {"proxy": "items"},
        "requestContext": {"http": {"method": "GET"}},
    }
    response = handler(event, "", item_usecase_mock, bid_usecase_mock)
    assert (
        '{"items": [{"id": "1", "name": "hoge", "image_src": "test.png", "description": "hoge", "start_price": 100, "bid_num": 0}]}'
        == response.get("body")
    )
