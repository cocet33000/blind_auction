import json

from Repository import BidRepository


def get_bids_by_user(user_name: str) -> dict:
    bids = BidRepository.getByUserName(user_name)
    return {"bids": [bid.to_dict() for bid in bids]}


if __name__ == "__main__":
    print(json.dumps(get_bids_by_user(user_name="hoge")))
