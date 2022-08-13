from __future__ import annotations

from main.usecase import QueryUseCase
from . import dynamo_db


class QueryUsecaseImpl(QueryUseCase):
    @staticmethod
    def get_bid_history(user_name: str):
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

        return bidhisory
