import datetime
import pytest
import uuid

from main.domain.auction import Auction, Period
from main.domain.auction import Status
from main.domain.shared.errors.errors import ProhibitedGenerationError


def test_外部からのauctionの生成はNG():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.OPEN
    START_DATETIME = datetime.datetime(2022, 10, 1, 0, 0, 0)
    END_DATETIME = datetime.datetime(2022, 10, 31, 0, 0, 0)
    with pytest.raises(ProhibitedGenerationError):
        Auction(ID, NAME, STATUS, Period(START_DATETIME, END_DATETIME))
