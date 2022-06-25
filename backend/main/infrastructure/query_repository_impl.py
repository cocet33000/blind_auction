from __future__ import annotations
from main.domain.query import QueryRepository
from main.domain.query.bid_history import BidHistory
from . import dynamo_db


class QueryReositoryImpl(QueryRepository):
    @staticmethod
    def get_bid_history(user_name: str) -> BidHistory:
        bidhisory = []
        bids = [
            bid.to_model()
            for bid in dynamo_db.Bid.bidsByUserNameIndex.query(hash_key=user_name)
        ]
        for bid in bids:
            item = dynamo_db.Item.get(hash_key=bid.bid_item_id, range_key="item")
            bidHistorySlice = {
                "item": {
                    "id": item.id,
                    "name": item.name,
                    "image_src": item.image_src,
                    "description": item.description,
                    "start_price": item.start_price,
                },
                "bid": {"price": bid.price, "bided_at": bid.bided_at},
            }
            bidhisory.append(bidHistorySlice)

        return BidHistory(user_name=user_name, bid_history=bidhisory)
