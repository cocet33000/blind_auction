from __future__ import annotations
import json

from main.presentation.lambda_handler import api_handler

from mock import Mock

from main.domain.shared import DomainException

from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase

from main.domain.item import Item
from main.domain.item import Status
from main.domain.value_object import Price

items = [
    Item.reconstruct(
        id="1",
        status=Status.BEFORE_AUCTION,
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
    )
]

item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)
auction_usecase_mock = Mock(spec=AuctionUseCase)

event = {
    "pathParameters": {"proxy": "items"},
    "requestContext": {"http": {"method": "GET"}},
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    item_usecase_mock.get_items.return_value = {
        "items": [item.to_dict() for item in items]
    }
    response: dict = api_handler(
        event, "", item_usecase_mock, bid_usecase_mock, auction_usecase_mock
    )

    assert (
        '{"items": [{"id": "1", "status": "before_auction", "name": "hoge", "image_src": "test.png", "description": "hoge", "start_price": 100, "bid_num": 0}]}'
        == response.get("body")
    )


def test_異常系():
    item_usecase_mock.get_items.side_effect = DomainException("NG")
    response: dict = api_handler(
        event, "", item_usecase_mock, bid_usecase_mock, auction_usecase_mock
    )
    body = json.loads(response.get("body"))

    assert response.get("statusCode") == 500
    assert body.get("message") == "NG"
