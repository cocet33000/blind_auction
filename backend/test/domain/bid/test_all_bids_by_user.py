import unittest
import datetime

import main.domain.value_object as value_object
import main.domain.bid as domain_bid


class TestBidModel(unittest.TestCase):
    def test_(self):
        BIDED_USER_NAME = "hoge"
        BID_ITEM_ID = "1"
        PRICE = 100
        BIDED_AT = datetime.datetime.now()

        bid_1 = domain_bid.Bid(
            bided_user_name=BIDED_USER_NAME,
            bid_item_id=BID_ITEM_ID,
            price=value_object.Price(PRICE),
            bided_at=BIDED_AT,
        )

        bid_2 = domain_bid.Bid(
            bided_user_name=BIDED_USER_NAME,
            bid_item_id=BID_ITEM_ID,
            price=value_object.Price(PRICE),
            bided_at=BIDED_AT,
        )
        bid_list = [bid_1, bid_2]
        all_bids_by_user = domain_bid.AllBidsByUser(bid_list)

        for _bid in all_bids_by_user:
            _bid: domain_bid.Bid = _bid
            self.assertEqual(BID_ITEM_ID, _bid.bid_item_id)
