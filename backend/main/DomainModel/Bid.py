from dataclasses import dataclass
from datetime import datetime


@dataclass
class Bid:
    bided_user_name: str
    bid_item_id: int
    price: int
    bided_at: datetime
