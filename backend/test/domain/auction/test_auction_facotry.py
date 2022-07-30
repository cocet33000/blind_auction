import datetime

from main.domain.auction import AuctionFactory


def test_auctionを生成():
    NAME = "test_auction"
    START_DATETIME = datetime.datetime(2022, 10, 1, 0, 0, 0)
    END_DATETIME = datetime.datetime(2022, 10, 31, 0, 0, 0)

    auction = AuctionFactory.create(NAME, START_DATETIME, END_DATETIME)

    assert auction.name() == NAME
    # 生成時は必ずCLOSE状態
    assert auction.isOpen() is False
