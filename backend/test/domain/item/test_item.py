import pytest
import uuid

from main.domain.item import Item
from main.domain.item import Status
from main.domain.value_object import Price
from main.domain.shared.errors import ProhibitedGenerationError


def test_itemを再構成():
    item = Item.reconstruct(
        id=str(uuid.uuid4()),
        status=Status.get_status("before_auction"),
        name="hoge",
        image_src="hoge",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
    )
    assert item.id is not None
    assert item.status == Status.BEFORE_AUCTION
    assert item.name == "hoge"
    assert item.image_src == "hoge"
    assert item.description == "hoge"
    assert item.start_price == 100
    assert item.bid_num == 0
    assert item.to_dict() == {
        "id": item.id,
        "status": item.status.value,
        "name": item.name,
        "image_src": item.image_src,
        "description": item.description,
        "start_price": item.start_price,
        "bid_num": item.bid_num,
    }


def test_外部からのitemの生成はNG():
    with pytest.raises(ProhibitedGenerationError):
        Item(
            id=str(uuid.uuid4()),
            status=Status.BEFORE_AUCTION,
            name="hoge",
            image_src="hoge",
            description="hoge",
            start_price=Price(100),
            bid_num=0,
        )
