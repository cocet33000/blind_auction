import logging

import DynamoDBModel
import Model
from .ItemRepository import ItemRepository


class BidRepository:
    @staticmethod
    def save(bid: Model.Bid) -> dict:
        item = ItemRepository.getByItemId(bid.bid_item_id)

        new_bid = DynamoDBModel.Bid(
            bided_at=bid.bided_at, bided_user_id=bid.bided_user_id, price=bid.price
        )

        try:
            if item.to_model().bid_num == 0:
                item.update(actions=[DynamoDBModel.Item.bids.set([new_bid])])
            else:
                item.update(
                    actions=[
                        DynamoDBModel.Item.bids.set(
                            DynamoDBModel.Item.bids.append([new_bid])
                        )
                    ]
                )

            return {"is_error": False}
        except Exception as e:
            logging.error(e)
            return {"is_error": True}
