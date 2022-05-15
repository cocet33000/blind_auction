from dataclasses import dataclass
from datetime import datetime


@dataclass
class Bid:
    bided_user_name: str
    bid_item_id: int
    price: int
    bided_at: datetime

    def __post_init__(self):
        if not (isinstance(self.bided_user_name, str) and isinstance(self.bid_item_id, int) and isinstance(self.price, int) and isinstance(self.bided_at, datetime)):
            raise TypeError
        if not (1 <= self.bid_item_id < 100000000):
            raise ValueError
        if not (0 <= self.price < 1000000):
            raise ValueError

    def to_dict(self) -> dict:
        return {
            "bided_user_name": self.bided_user_name,
            "bid_item_id": self.bid_item_id,
            "price": self.price,
            "bided_at": self.bided_at.strftime("%Y/%m/%d %H:%M"),
        }
