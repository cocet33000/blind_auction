import uuid

from main.domain.value_object import Price
from main.domain.item import Item, Status
from main.infrastructure.item_repository_impl import ItemRepositoryImpl


def test_正常系():
    item = Item.reconstruct(
        id=str(uuid.uuid4()),
        status=Status.BEFORE_AUCTION,
        name="hoge",
        image_src="hoge",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
    )
    res = ItemRepositoryImpl.save(item)
    assert res.get("is_error") is False
