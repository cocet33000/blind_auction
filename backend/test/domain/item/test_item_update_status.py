import uuid

from main.domain.item import Item
from main.domain.item import Status
from main.domain.value_object import Price


def test_正常系_itemのステータスをオークション中に():
    item = Item.reconstruct(
        id=str(uuid.uuid4()),
        status=Status.BEFORE_AUCTION,
        name="hoge",
        image_src="hoge",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id=str(uuid.uuid4()),
    )

    assert item.status == Status.BEFORE_AUCTION
    item.to_up_for_auction()
    assert item.status == Status.UP_FOR_AUCTION


def test_正常系_itemのステータスを売り切れに():
    item = Item.reconstruct(
        id=str(uuid.uuid4()),
        status=Status.UP_FOR_AUCTION,
        name="hoge",
        image_src="hoge",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id=str(uuid.uuid4()),
    )

    assert item.status == Status.UP_FOR_AUCTION
    item.to_sold_out()
    assert item.status == Status.SOLD_OUT
