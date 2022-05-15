import unittest
import datetime
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent / "main"))
from DomainModel import Bid


class TestBidModel(unittest.TestCase):
    def test_input_valid_parameter(self):
        
        TEST_BIDED_AT = datetime.datetime.now()
        input_param_list = [
            ("hoge", 1, 0, TEST_BIDED_AT ),
            ("hoge", 99999999, 0, TEST_BIDED_AT),
            ("hoge", 1, 999999, TEST_BIDED_AT),
        ]
        for BIDED_USER_NAME, BID_ITEM_ID, PRICE, BIDED_AT in input_param_list:
            with self.subTest(BIDED_USER_NAME=BIDED_USER_NAME, BID_ITEM_ID=BID_ITEM_ID, PRICE=PRICE, BIDED_AT=BIDED_AT):
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


    def test_input_invalid_parameter_except_TypeError(self):
        TEST_BIDED_AT = datetime.datetime.now()
        input_param_list = [
            (1, 1, 0, TEST_BIDED_AT),
            ("hoge", "aaa", 0, TEST_BIDED_AT),
            ("hoge", 1, "aaa", TEST_BIDED_AT),
            ("hoge", 1, 0, "aaa"),
        ]
        for BIDED_USER_NAME, BID_ITEM_ID, PRICE, BIDED_AT in input_param_list:
            with self.subTest(BIDED_USER_NAME=BIDED_USER_NAME, BID_ITEM_ID=BID_ITEM_ID, PRICE=PRICE, BIDED_AT=BIDED_AT):
                with self.assertRaises(TypeError):
                    Bid(
                        bided_user_name=BIDED_USER_NAME,
                        bid_item_id=BID_ITEM_ID,
                        price=PRICE,
                        bided_at=BIDED_AT,
                    )


    def test_input_invalid_parameter_except_ValueError(self):
        TEST_BIDED_AT = datetime.datetime.now()
        input_param_list = [
            ("hoge", -1, 0, TEST_BIDED_AT),
            ("hoge", 0, 0, TEST_BIDED_AT),
            ("hoge", 100000000, 0, TEST_BIDED_AT),
            ("hoge", 1, -1, TEST_BIDED_AT),
            ("hoge", 1, 1000000, TEST_BIDED_AT),
        ]
        for BIDED_USER_NAME, BID_ITEM_ID, PRICE, BIDED_AT in input_param_list:
            with self.subTest(BIDED_USER_NAME=BIDED_USER_NAME, BID_ITEM_ID=BID_ITEM_ID, PRICE=PRICE, BIDED_AT=BIDED_AT):
                with self.assertRaises(ValueError):
                    Bid(
                        bided_user_name=BIDED_USER_NAME,
                        bid_item_id=BID_ITEM_ID,
                        price=PRICE,
                        bided_at=BIDED_AT,
                    )


if __name__ == "__main__":
    unittest.main()
