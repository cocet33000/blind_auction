from __future__ import annotations
import json
from datetime import datetime

from main.presentation.lambda_handler import api_handler

from mock import Mock

from main.domain.auction import Auction
from main.domain.auction import Status

from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase

item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)
auction_usecase_mock = Mock(spec=AuctionUseCase)

auctions = [
    Auction.reconstruct(
        id="1",
        name="hoge",
        status=Status.OPEN,
        start_datetime=datetime(2020, 1, 1, 0, 0),
        end_datetime=datetime(2020, 3, 1, 0, 0),
    )
]

event = {
    "pathParameters": {"proxy": "auctions"},
    "requestContext": {"http": {"method": "GET"}},
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    response: dict = api_handler(event, "", item_usecase_mock, bid_usecase_mock, auction_usecase_mock)  # type: ignore
    assert response.get("statusCode") == 200
    assert (
        response.get("body")
        == '{"has_next:": false, "auctions": [{"id": "1", "name": "auction001"}]}'
    )
