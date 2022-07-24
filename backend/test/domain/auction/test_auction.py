import datetime

from main.domain.auction import Auction
from main.domain.auction import Status


def test_正常系_auctionインスタンスを生成():
    NAME = "test_auction"
    STATUS = Status.OPEN
    START_DATETIME = datetime.datetime(2022, 10, 1, 0, 0, 0)
    END_DATETIME = datetime.datetime(2022, 10, 31, 0, 0, 0)
    auction = Auction(NAME, STATUS, START_DATETIME, END_DATETIME)
    assert auction is not None
