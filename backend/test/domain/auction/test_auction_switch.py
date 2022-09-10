import uuid
from datetime import datetime

from main.domain.auction import Auction
from main.domain.auction import AuctionEvent
from main.domain.auction import Status


def test_正常系_オークション開始_イベント発行():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.CLOSED
    START_DATETIME = datetime(2022, 10, 5, 10, 0, 0)
    END_DATETIME = datetime(2022, 10, 31, 0, 0, 0)

    NOW_DATETIME = datetime(2022, 10, 5, 10, 0, 1)

    auction = Auction.reconstruct(ID, NAME, STATUS, START_DATETIME, END_DATETIME)
    assert not auction.isOpen()

    auction_event = auction.switchStatus(now_datetime=NOW_DATETIME)

    assert auction.isOpen()
    assert auction_event == AuctionEvent(
        auction_id=ID,
        auction_name=NAME,
        type=Status.OPEN,
    )


def test_正常系_オークション開始済み_イベント発行無し():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.OPEN
    START_DATETIME = datetime(2022, 10, 5, 10, 0, 0)
    END_DATETIME = datetime(2022, 10, 31, 0, 0, 0)

    NOW_DATETIME = datetime(2022, 10, 5, 10, 0, 1)

    auction = Auction.reconstruct(ID, NAME, STATUS, START_DATETIME, END_DATETIME)
    assert auction.isOpen()

    auction_event = auction.switchStatus(now_datetime=NOW_DATETIME)

    assert auction.isOpen()
    assert auction_event is None


def test_正常系_オークション終了_イベント発行():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.OPEN
    START_DATETIME = datetime(2022, 10, 5, 10, 0, 0)
    END_DATETIME = datetime(2022, 10, 31, 0, 0, 0)

    NOW_DATETIME = datetime(2022, 10, 31, 10, 0, 1)
    auction = Auction.reconstruct(ID, NAME, STATUS, START_DATETIME, END_DATETIME)
    assert auction.isOpen()

    auction_event = auction.switchStatus(now_datetime=NOW_DATETIME)

    assert not auction.isOpen()
    assert auction_event == AuctionEvent(
        auction_id=ID,
        auction_name=NAME,
        type=Status.CLOSED,
    )


def test_正常系_オークション終了済み_イベント発行なし():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.CLOSED
    START_DATETIME = datetime(2022, 10, 5, 10, 0, 0)
    END_DATETIME = datetime(2022, 10, 31, 0, 0, 0)

    NOW_DATETIME = datetime(2022, 10, 31, 10, 0, 1)
    auction = Auction.reconstruct(ID, NAME, STATUS, START_DATETIME, END_DATETIME)
    assert not auction.isOpen()

    auction_event = auction.switchStatus(now_datetime=NOW_DATETIME)

    assert not auction.isOpen()
    assert auction_event is None
