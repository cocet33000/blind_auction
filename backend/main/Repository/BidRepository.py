from __future__ import annotations
import logging

from . import DynamoDBModel
import DomainModel


class BidRepository:
    @staticmethod
    def save(bid: DomainModel.Bid) -> dict:
        item = DynamoDBModel.Item.get(bid.bid_item_id)

        new_bid = DynamoDBModel.Bid(
            bided_at=bid.bided_at, bided_user_name=bid.bided_user_name, price=bid.price
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

    @staticmethod
    def getByUserName(user_name: str) -> list[DomainModel.Bid]:
        def is_bid_by_user_name(bids: list[DynamoDBModel.Bid], user_name: str) -> bool:
            return user_name in list(map(lambda bid: bid.bided_user_name, bids))

        items = DynamoDBModel.Item.scan()
        return [
            item.bids[0].to_model(item_id=item.id)
            for item in filter(
                lambda item: is_bid_by_user_name(item.bids, user_name)
                if item.bids
                else False,
                items,
            )
        ]
