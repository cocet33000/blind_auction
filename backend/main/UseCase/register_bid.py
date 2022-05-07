import json
import datetime

from DomainModel import Bid
from Repository import BidRepository


def register_bid(user_id: int, item_id: int, price: int) -> dict:
    bid = Bid(
        bided_user_id=user_id,
        bid_item_id=item_id,
        bided_at=datetime.datetime.now(),
        price=price,
    )
    return BidRepository.save(bid)


if __name__ == "__main__":
    print(json.dumps(register_bid(user_id=1, item_id=9, price=10000)))
