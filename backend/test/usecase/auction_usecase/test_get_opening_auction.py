from __future__ import annotations

from mock import Mock
from datetime import datetime

from injector import Injector, Module, singleton

from main.domain.auction import Auction
from main.domain.auction import Status
from main.domain.auction import AuctionRepository
from main.domain.shared import EventPublisher

from main.usecase import AuctionUseCase

event_publisher_mock = Mock(spec=EventPublisher)
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
        status=Status.CLOSED,
        start_datetime=datetime(2020, 1, 1, 0, 0, 0),
        end_datetime=datetime(2020, 3, 1, 0, 0, 0),
    ),
]


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(AuctionRepository, to=auction_repository_mock)
        binder.bind(EventPublisher, to=event_publisher_mock)


def test_正常系():
    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    auction = auction_usecase.get_opening_auction()

    assert auction.to_dict().get("id") == "1"
