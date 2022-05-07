import unittest
import datetime
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent / "main"))
from DomainModel import Bid


class TestBidModel(unittest.TestCase):
    def test_bidモデルを作成(self):
        BIDED_USER_NAME = "hoge"
        BID_ITEM_ID = 1
        PRICE = 100
        BIDED_AT = datetime.datetime.now()

        bid = Bid(
            bided_user_name=BIDED_USER_NAME,
            bid_item_id=BID_ITEM_ID,
            price=PRICE,
            bided_at=BIDED_AT,
        )

        self.assertEqual(bid.bided_user_name, BIDED_USER_NAME)
        self.assertEqual(bid.bid_item_id, BID_ITEM_ID)
        self.assertEqual(bid.price, PRICE)
        self.assertEqual(bid.bided_at, BIDED_AT)

    def test_priceに文字列はNG(self):
        BIDED_USER_NAME = "hoge"
        BID_ITEM_ID = 1
        PRICE_STR = "HOGE"
        BIDED_AT = datetime.datetime.now()

        with self.assertRaises(TypeError):
            Bid(
                bided_user_name=BIDED_USER_NAME,
                bid_item_id=BID_ITEM_ID,
                price=PRICE_STR,
                bided_at=BIDED_AT,
            )


if __name__ == "__main__":
    unittest.main()
