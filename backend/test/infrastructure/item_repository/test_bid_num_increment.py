import uuid

from main.infrastructure.item_repository_impl import ItemRepositoryImpl

from main.domain.value_object import Price
from main.domain.item import Item, Status


def test_正常系():
    item_id = str(uuid.uuid4())

    item = Item.reconstruct(
        id=item_id,
        status=Status.BEFORE_AUCTION,
        name="hoge",
        image_src="hoge",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id=str(uuid.uuid4()),
    )
    ItemRepositoryImpl.save(item)

    ItemRepositoryImpl.bidNumIncrement(item_id)
