from __future__ import annotations
from datetime import datetime
import uuid

from mock import Mock

from injector import Injector, Module, singleton

from main.domain.auction import AuctionRepository
from main.domain.auction import AuctionEvent
from main.domain.auction import Auction, Status
from main.domain.shared import EventPublisher
from main.domain.shared.event import event_publisher
from main.usecase import AuctionUseCase

auction_repository_mock = Mock(spec=AuctionRepository)
event_publisher_mock = Mock(spec=EventPublisher)
event_publisher_mock.publish.return_value = {"is_error": False}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(AuctionRepository, to=auction_repository_mock)
        binder.bind(EventPublisher, to=event_publisher_mock)


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

    assert event_publisher_mock.publish.call_count == 1
    assert auction_repository_mock.save.call_count == 1
    assert auction_event == AuctionEvent(
        auction_id=ID,
        auction_name=NAME,
        type=Status.OPEN,
    )
