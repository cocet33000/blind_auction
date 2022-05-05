from re import I
from DynamoDBModel.Item import Item as DynamoDBItem
from DynamoDBModel.Item import Bid as DynamoDBBid
from Model.Bid import Bid
from Repository.ItemRepository import ItemRepository


class BidRepository:
    @staticmethod
    def save(bid: Bid) -> dict:
        item = ItemRepository.getByItemId(bid.bid_item_id)

        new_bid = DynamoDBBid(
            bided_at=bid.bided_at, bided_user_id=bid.bided_user_id, price=bid.price
        )

        try:
            if item.to_model().bid_num == 0:
                item.update(actions=[DynamoDBItem.bids.set([new_bid])])
            else:
                item.update(
                    actions=[DynamoDBItem.bids.set(DynamoDBItem.bids.append([new_bid]))]
                )

            return {"is_error": False}
        except Exception as e:
            return {"is_error": True}
