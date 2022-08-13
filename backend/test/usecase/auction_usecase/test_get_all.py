from __future__ import annotations

from mock import Mock
from datetime import datetime

from injector import Injector, Module, singleton

from main.domain.auction import Auction
from main.domain.auction import Status
from main.domain.auction import AuctionRepository

from main.usecase import AuctionUseCase

auction_repository_mock = Mock(spec=AuctionRepository)
auction_repository_mock.getAll.return_value = [
    Auction.reconstruct(
        id="1",
        name="auction001",
        status=Status.OPEN,
        start_datetime=datetime(2020, 1, 1, 0, 0, 0),
        end_datetime=datetime(2020, 3, 1, 0, 0, 0),
    ),
    Auction.reconstruct(
        id="2",
        name="auction002",
        status=Status.OPEN,
        start_datetime=datetime(2020, 1, 1, 0, 0, 0),
        end_datetime=datetime(2020, 3, 1, 0, 0, 0),
    ),
]


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(AuctionRepository, to=auction_repository_mock)


def test_正常系():
    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    auctions = auction_usecase.get_auctions_all()

    assert auctions[0].to_dict().get("id") == "1"
    assert auctions[1].to_dict().get("id") == "2"
