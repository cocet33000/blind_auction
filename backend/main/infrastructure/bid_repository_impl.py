from __future__ import annotations
import logging

from . import dynamo_db
from main.domain.bid import Bid
from main.domain.bid import AllBidsByUser
from main.domain.bid import BidRepository


class BidRepositoryImpl(BidRepository):
    @staticmethod
    def save(bid: Bid) -> dict:
        new_bid = dynamo_db.Bid(hash_key=bid.bid_item_id, range_key=bid.id)
        new_bid.price = bid.price
        new_bid.bided_user_name = bid.bided_user_name
        new_bid.bided_at = bid.bided_at
        new_bid.save()

        try:
            new_bid.save()
            return {"is_error": False, "id": bid.id}
        except Exception as e:
            logging.error(e)
            return {"is_error": True}

    @staticmethod
    def getByUserName(user_name) -> AllBidsByUser:
        bids = dynamo_db.Bid.bidsByUserNameIndex.query(hash_key=user_name)
        return AllBidsByUser(bids)
