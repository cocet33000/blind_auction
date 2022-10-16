from main.presentation.lambda_handler.serialize import home_get_response_serialize

from datetime import datetime

from main.domain.value_object import Price

from main.domain.auction import Auction, Status as AuctionStatus
from main.domain.item import Item, Status as ItemStatus

auction = Auction.reconstruct(
    id="1",
    name="test",
    status=AuctionStatus.OPEN,
    start_datetime=datetime(2020, 1, 1, 0, 0, 0),
    end_datetime=datetime(2020, 1, 1, 0, 0, 0),
)

items = [
    Item.reconstruct(
        id="hoge",
        status=ItemStatus.BEFORE_AUCTION,
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id="uuid",
    )
]


def test_正常系():

    home_get_response = home_get_response_serialize(auction, items)

    assert home_get_response["auction"]["id"] == "1"
    assert home_get_response["items"]["items"][0]["id"] == "hoge"
