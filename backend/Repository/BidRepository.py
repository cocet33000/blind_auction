from DynamoDBModel.Item import Item as DynamoDBItem
from Model.Bid import Bid
from Repository.ItemRepository import ItemRepository


class BidRepository:
    @staticmethod
    def save(bid: Bid) -> dict:
        item_repository = ItemRepository()
        item = item_repository.getByItemId(bid.bid_item_id)

        new_bid = {
            "bided_at": bid.bided_at,
            "bided_user_id": bid.bided_user_id,
            "price": bid.price,
        }

        if item.to_model().bided_num == 0:
            new_bids = [new_bid]
        else:
            item.bids.append(
                {
                    "bided_at": bid.bided_at,
                    "bided_user_id": bid.bided_user_id,
                    "price": bid.price,
                }
            )
            new_bids = item.bids

        try:
            item.update(actions=[DynamoDBItem.bids.set(new_bids)])
            return {"is_error": False}
        except Exception as e:
            print(e)
            return {"is_error": True}
