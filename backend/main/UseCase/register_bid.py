import json
import datetime

from DomainModel import Bid
from Infrastructure import BidRepositoryImpl


def register_bid(user_name: str, item_id: int, price: int) -> dict:
    bid = Bid(
        bided_user_name=user_name,
        bid_item_id=item_id,
        bided_at=datetime.datetime.now(),
        price=price,
    )
    return BidRepositoryImpl.save(bid)


if __name__ == "__main__":
    print(json.dumps(register_bid(user_name="test", item_id=9, price=10000)))
