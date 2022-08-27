from __future__ import annotations
from datetime import datetime
import uuid

from mock import Mock

from injector import Injector, Module, singleton

from main.domain.auction import AuctionRepository
from main.domain.auction import Auction, Status

from main.usecase import AuctionUseCase

auction_repository_mock = Mock(spec=AuctionRepository)


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(AuctionRepository, to=auction_repository_mock)


def test_正常系():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.CLOSED
    START_DATETIME = datetime(2022, 1, 5, 10, 0, 0)
    END_DATETIME = datetime(2022, 10, 31, 0, 0, 0)

    auction = Auction.reconstruct(ID, NAME, STATUS, START_DATETIME, END_DATETIME)
    auction_repository_mock.getById.return_value = auction

    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    auction_id = ID
    auction_event = auction_usecase.switch_auction(auction_id)

    assert auction_event.get("id") == auction_id
    assert auction_event.get("status") == "OPEN"
