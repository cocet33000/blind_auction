from __future__ import annotations
from pydoc import resolve

from main.presentation.lambda_handler import api_handler

from mock import Mock

from main.domain.shared import DomainException

from main.usecase import ItemUseCase
from main.usecase import BidUseCase

from main.domain.item import Item
from main.domain.value_object import Price

items = [
    Item.reconstruct(
        id="1",
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
    )
]

item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)

event = {
    "pathParameters": {"proxy": "items"},
    "requestContext": {"http": {"method": "GET"}},
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    item_usecase_mock.get_items.return_value = {
        "items": [item.to_dict() for item in items]
    }
    response: dict = api_handler(event, "", item_usecase_mock, bid_usecase_mock)

    assert (
        '{"items": [{"id": "1", "name": "hoge", "image_src": "test.png", "description": "hoge", "start_price": 100, "bid_num": 0}]}'
        == response.get("body")
    )


def test_異常系():
    item_usecase_mock.get_items.side_effect = DomainException("NG")
    response: dict = api_handler(event, "", item_usecase_mock, bid_usecase_mock)

    assert response.get("statusCode") == 500
    assert response.get("body").get("message") == "NG"
