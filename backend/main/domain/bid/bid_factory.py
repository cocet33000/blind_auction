from injector import inject

from .bid import Bid
from ..value_object.price import Price
import datetime

from ..item import Item
from ..item import ItemRepository


class BidFactory:
    @inject
    def __init__(self, ItemRepositoryImpl: ItemRepository):
        self.item_repository = ItemRepositoryImpl

    def create(self, name: str, item_id: int, price: int) -> Bid:
        bid_price: Price = Price(price)
        target_item: Item = self.item_repository.getByItemId(item_id)

        if bid_price <= target_item.start_price:
            raise ValueError

        return Bid(
            bided_user_name=name,
            bid_item_id=item_id,
            price=bid_price,
            bided_at=datetime.datetime.now(),
        )
