from DynamoDBModel.Item import Item
from Repository.ItemRepository import ItemRepository


class BidRepository():
    def save(self, bid):
        item_repository = ItemRepository()
        item = item_repository.getByItemId(bid.bid_item_id)

        new_bid = {
            "bided_at": bid.bided_at,
            "bided_user_id": bid.bided_user_id,
            "price": bid.price
        }

        if item.convert_to().bided_num == 0:
            new_bids = [new_bid]
        else:
            item.bids.append({
                        "bided_at": bid.bided_at,
                        "bided_user_id": bid.bided_user_id,
                        "price": bid.price
                    })
            new_bids = item.bids

        try:
            item.update(actions=[
                Item.bids.set(
                    new_bids
                )
            ])
            return "OK"
        except Exception as e:
            print(e)
            return "NG"

