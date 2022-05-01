import datetime

from Model.Bid import Bid
from Repository.BidRepository import BidRepository

if __name__ == "__main__":
    bid = Bid(
        bided_user_id=2,
        bid_item_id=68,
        bided_at=datetime.datetime.now(),
        price=10000,
    )
    bid_repository = BidRepository()
    bid_repository.save(bid)
