from __future__ import annotations
from datetime import datetime
import json

from main.presentation.lambda_handler import api_handler

from main.domain.shared import DomainException

from mock import Mock

from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase
from main.usecase import QueryUseCase

item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)
auction_usecase_mock = Mock(spec=AuctionUseCase)
query_usecase_mock = Mock(spec=QueryUseCase)

event = {
    "pathParameters": {"proxy": "bids"},
    "requestContext": {"http": {"method": "GET"}},
    "queryStringParameters": {"user_name": "test"},
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    query_usecase_mock.get_bid_history.return_value = [
        {
            "item": {
                "id": "1",
                "name": "test",
                "image_src": "test",
                "description": "test",
                "start_price": 100,
            },
            "bid": {"price": 100, "bided_at": datetime.now()},
        },
    ]
    response: dict = api_handler(
        event,
        "",
        item_usecase_mock,
        bid_usecase_mock,
        auction_usecase_mock,
        query_usecase_mock,
    )  # type: ignore

    assert response["statusCode"] == 200
