from __future__ import annotations
from datetime import datetime

from main.presentation.lambda_handler import api_handler

from mock import Mock


from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.usecase import AuctionUseCase
from main.usecase import QueryUseCase

from main.domain.item import Item
from main.domain.item import Status

from main.domain.auction import Auction, Status as AuctionStatus

from main.domain.value_object import Price


auction = Auction.reconstruct(
    id="1",
    name="test",
    status=AuctionStatus.OPEN,
    start_datetime=datetime(2020, 1, 1, 0, 0, 0),
    end_datetime=datetime(2020, 1, 1, 0, 0, 0),
)

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
    auction_usecase_mock.get_opening_auction.return_value = auction
    item_usecase_mock.get_items_by_auction_id.return_value = items

    api_handler(
        event,
        "",
        item_usecase_mock,
        bid_usecase_mock,
        auction_usecase_mock,
        query_usecase_mock,
    )  # type: ignore
