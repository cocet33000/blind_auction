from dataclasses import dataclass
from datetime import datetime

from ..value_object.price import Price


@dataclass
class Bid:
    bided_user_name: str
    bid_item_id: int
    price: Price
    bided_at: datetime

    def __post_init__(self):
        if not isinstance(self.price, Price):
            raise TypeError

    def to_dict(self) -> dict:
        return {
            "bided_user_name": self.bided_user_name,
            "bid_item_id": self.bid_item_id,
            "price": self.price,
            "bided_at": self.bided_at.strftime("%Y/%m/%d %H:%M"),
        }
