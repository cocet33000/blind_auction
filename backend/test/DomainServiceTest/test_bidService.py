import unittest
import datetime
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent / "main"))
from DomainService import BidFactory


# class TestBidFactory(unittest.TestCase):
#     def test_ユーザーは(self):
#         既に入札ずみのユーザーID = "hoge"
#         BID_ITEM_ID = 1
#         PRICE = 100
#         BIDED_AT = datetime.datetime.now()

#         bid = Bid(
#             bided_user_name=BIDED_USER_NAME,
#             bid_item_id=BID_ITEM_ID,
#             price=PRICE,
#             bided_at=BIDED_AT,
#         )

#         # 既に入札済みのユーザーの場合は例外を投げる
#         with self.assertRaises(TypeError):
#             BidFactory.Create(
#                 bided_user_name=既に入札ずみのユーザーID,
#                 bid_item_id=BID_ITEM_ID,
#                 price=PRICE_STR,
#                 bided_at=BIDED_AT,
#             )
