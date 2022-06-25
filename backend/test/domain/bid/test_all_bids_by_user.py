import uuid
import pytest
import datetime

import main.domain.value_object as value_object
import main.domain.bid as domain_bid


def test_():
    BID_ID_1 = "bid" + str(uuid.uuid4())
    BID_ID_2 = "bid" + str(uuid.uuid4())
    BIDED_USER_NAME = "hoge"
    BID_ITEM_ID = "1"
    PRICE = 100
    BIDED_AT = datetime.datetime.now()

    bid_1 = domain_bid.Bid(
        id=BID_ID_1,
        bided_user_name=BIDED_USER_NAME,
        bid_item_id=BID_ITEM_ID,
        price=value_object.Price(PRICE),
        bided_at=BIDED_AT,
    )

    bid_2 = domain_bid.Bid(
        id=BID_ID_2,
        bided_user_name=BIDED_USER_NAME,
        bid_item_id=BID_ITEM_ID,
        price=value_object.Price(PRICE),
        bided_at=BIDED_AT,
    )
    bid_list = [bid_1, bid_2]
    all_bids_by_user = domain_bid.AllBidsByUser(bid_list)

    for _bid in all_bids_by_user:
        _bid: domain_bid.Bid = _bid
        assert BID_ITEM_ID == _bid.bid_item_id
