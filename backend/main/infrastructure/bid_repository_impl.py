from __future__ import annotations
import logging

from . import dynamo_db
from main.domain.bid import Bid
from main.domain.bid import BidsByUser
from main.domain.bid import BidRepository


class BidRepositoryImpl(BidRepository):
    @staticmethod
    def save(bid: Bid) -> dict:
        item = dynamo_db.Item.get(bid.bid_item_id)

        new_bid = dynamo_db.Bid(
            bided_at=bid.bided_at, bided_user_name=bid.bided_user_name, price=bid.price
        )

        try:
            if item.to_model().bid_num == 0:
                item.update(actions=[dynamo_db.Item.bids.set([new_bid])])
            else:
                item.update(
                    actions=[
                        dynamo_db.Item.bids.set(dynamo_db.Item.bids.append([new_bid]))
                    ]
                )

            return {"is_error": False}
        except Exception as e:
            logging.error(e)
            return {"is_error": True}

    @staticmethod
    def getByUserName(user_name):
        def is_bid_by_user_name(bids: list[dynamo_db.Bid], user_name: str) -> bool:
            return user_name in list(map(lambda bid: bid.bided_user_name, bids))

        items = dynamo_db.Item.scan()
        return BidsByUser(
            [
                item.bids[0].to_model(item_id=item.id)
                for item in filter(
                    lambda item: is_bid_by_user_name(item.bids, user_name)
                    if item.bids
                    else False,
                    items,
                )
            ]
        )
