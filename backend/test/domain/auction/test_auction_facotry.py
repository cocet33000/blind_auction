import pytest
import datetime

from injector import Injector, Module, singleton
from mock import Mock

from main.domain.shared.errors.errors import DomainException
from main.domain.auction import AuctionFactory, Auction, Status
from main.domain.auction.auction_repository import AuctionRepository

auction_repository_mock = Mock(spec=AuctionRepository)
auction_repository_mock.getAll.return_value = [
    Auction.reconstruct(
        id="1",
        name="test_auction",
        status=Status.CLOSED,
        start_datetime=datetime.datetime(2022, 10, 1, 0, 0, 0),
        end_datetime=datetime.datetime(2022, 10, 31, 0, 0, 0),
    )
]


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(AuctionRepository, to=auction_repository_mock)


def test_auctionを生成():
    injector = Injector([DIModule()])
    auction_factory = injector.get(AuctionFactory)

    NAME = "test_auction"
    START_DATETIME = datetime.datetime(2022, 11, 1, 0, 0, 0)
    END_DATETIME = datetime.datetime(2022, 11, 30, 0, 0, 0)

    auction = auction_factory.create(NAME, START_DATETIME, END_DATETIME)

    assert auction.name() == NAME
    # 生成時は必ずCLOSE状態
    assert auction.isOpen() is False


def test_登録済みのオークションと開催期間がかぶるのはNG_1():
    injector = Injector([DIModule()])
    auction_factory = injector.get(AuctionFactory)

    NAME = "test_auction"
    START_DATETIME = datetime.datetime(2022, 10, 31, 0, 0, 0)
    END_DATETIME = datetime.datetime(2022, 11, 1, 0, 0, 0)

    with pytest.raises(DomainException):
        auction_factory.create(NAME, START_DATETIME, END_DATETIME)


def test_登録済みのオークションと開催期間がかぶるのはNG_2():
    injector = Injector([DIModule()])
    auction_factory = injector.get(AuctionFactory)

    NAME = "test_auction"
    START_DATETIME = datetime.datetime(2022, 9, 1, 0, 0, 0)
    END_DATETIME = datetime.datetime(2022, 10, 1, 0, 0, 0)

    with pytest.raises(DomainException):
        auction_factory.create(NAME, START_DATETIME, END_DATETIME)
