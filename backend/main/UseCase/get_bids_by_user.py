import json

from Repository import BidRepository
from Repository import ItemRepository


def get_bids_by_user(user_name: str) -> dict:
    bids = BidRepository.getByUserName(user_name)

    # 可読性と再利用性のために、N+1クエリを許容しているが、必要に応じてリファクタリングする
    items = [ItemRepository.getByItemId(bid.bid_item_id) for bid in bids]

    return {
        "bids": [bid.to_dict() for bid in bids],
        "items": [item.to_dict() for item in items],
    }


if __name__ == "__main__":
    print(json.dumps(get_bids_by_user(user_name="hoge")))
