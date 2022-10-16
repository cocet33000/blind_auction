from __future__ import annotations
import json
import uuid

from main.presentation.lambda_handler import api_handler

from mock import Mock

from main.domain.shared import DomainException

from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase
from main.usecase import QueryUseCase

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
        auction_id="uuid",
    )
]

item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)
auction_usecase_mock = Mock(spec=AuctionUseCase)
query_usecase_mock = Mock(spec=QueryUseCase)

event = {
    "pathParameters": {"proxy": "home"},
    "requestContext": {"http": {"method": "GET"}},
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    item_usecase_mock.get_items.return_value = {
        "items": [item.to_dict() for item in items]
    }
    response: dict = api_handler(
        event,
        "",
        item_usecase_mock,
        bid_usecase_mock,
        auction_usecase_mock,
        query_usecase_mock,
    )  # type: ignore

    assert (
        '{"auction": {"id": "1", "name": "test", "start_date": "2020-01-01T00:00:00", "end_date": "2020-01-01T00:00:00"}, "items": {"has_next": false, "items": [{"id": "1", "name": "test", "image_src": "https://example.com", "description": "test", "start_price": 1000, "bid_num": 0}]}}'
        == response.get("body")
    )
