from dataclasses import dataclass
from datetime import datetime


@dataclass
class Bid:
    bided_user_id: int
    bid_item_id: int
    price: int
    bided_at: datetime
