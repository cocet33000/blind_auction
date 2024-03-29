from __future__ import annotations
from datetime import datetime
import json
from main.presentation.lambda_handler import api_handler


from mock import Mock

from main.domain.auction import AuctionEvent
from main.domain.auction import Status

from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase
from main.usecase import QueryUseCase


item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)
auction_usecase_mock = Mock(spec=AuctionUseCase)
query_usecase_mock = Mock(spec=QueryUseCase)

event = {
    "pathParameters": {"proxy": "commands/auctions"},
    "requestContext": {"http": {"method": "POST"}},
    "body": """{}""",
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    auction_usecase_mock.switch_auction.return_value = [
        AuctionEvent(
            auction_id="hoge",
            auction_name="auction01",
            type=Status.OPEN,
        )
    ]
    response: dict = api_handler(
        event,
        "",
        item_usecase_mock,
        bid_usecase_mock,
        auction_usecase_mock,
        query_usecase_mock,
    )  # type: ignore

    assert response.get("statusCode") == 200
    assert response.get("body") == json.dumps(
        {
            "events": [
                {
                    "id": "hoge",
                    "name": "auction01",
                    "status": Status.OPEN.name,
                }
            ]
        }
    )
