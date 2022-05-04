import json
import datetime

from Model.Bid import Bid
from Repository.BidRepository import BidRepository


def bid(bided_user_id: int, bid_item_id: int, bid_price: int):
    bid = Bid(
        bided_user_id=bided_user_id,
        bid_item_id=bid_item_id,
        bided_at=datetime.datetime.now(),
        price=bid_price,
    )
    return BidRepository.save(bid)


if __name__ == "__main__":
    print(json.dumps(bid(bided_user_id=1, bid_item_id=2, bid_price=10000)))
