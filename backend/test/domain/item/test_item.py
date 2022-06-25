import uuid

from main.domain.item import Item
from main.domain.value_object import Price


def test_itemを生成():
    item = Item(
        id=str(uuid.uuid4()),
        name="hoge",
        image_src="hoge",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
    )
    assert item.id is not None
    assert item.name == "hoge"
    assert item.image_src == "hoge"
    assert item.description == "hoge"
    assert item.start_price == 100
    assert item.bid_num == 0
    assert item.to_dict() == {
        "id": item.id,
        "name": item.name,
        "image_src": item.image_src,
        "description": item.description,
        "start_price": item.start_price,
        "bid_num": item.bid_num,
    }
