from __future__ import annotations
from datetime import datetime
from datetime import timedelta
import uuid

from mock import Mock

from injector import Injector, Module, singleton

from main.domain.auction import AuctionRepository
from main.domain.auction import AuctionEvent
from main.domain.auction import Auction, Status
from main.domain.shared import EventPublisher
from main.usecase import AuctionUseCase

auction_repository_mock = Mock(spec=AuctionRepository)
event_publisher_mock = Mock(spec=EventPublisher)
event_publisher_mock.publish.return_value = {"is_error": False}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(AuctionRepository, to=auction_repository_mock)
        binder.bind(EventPublisher, to=event_publisher_mock)


def test_正常系_オークション開始_イベント発行():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.CLOSED
    START_DATETIME = datetime.now() - timedelta(days=1)
    END_DATETIME = datetime.now() + timedelta(days=1)
    auction_repository_mock.getAll.return_value = [
        Auction.reconstruct(
            id=ID,
            name=NAME,
            status=STATUS,
            start_datetime=START_DATETIME,
            end_datetime=END_DATETIME,
        )
    ]

    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    # Mockの呼び出し回数を初期化
    event_publisher_mock.publish.call_count = 0
    auction_repository_mock.save.call_count = 0

    auction_events = auction_usecase.switch_auction()

    assert event_publisher_mock.publish.call_count == 1
    assert auction_repository_mock.save.call_count == 1
    assert auction_events == [
        AuctionEvent(
            auction_id=ID,
            auction_name=NAME,
            type=Status.OPEN,
        )
    ]


def test_正常系_オークション開始済み_イベント発行なし():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.OPEN
    START_DATETIME = datetime.now() - timedelta(days=1)
    END_DATETIME = datetime.now() + timedelta(days=1)
    auction_repository_mock.getAll.return_value = [
        Auction.reconstruct(
            id=ID,
            name=NAME,
            status=STATUS,
            start_datetime=START_DATETIME,
            end_datetime=END_DATETIME,
        )
    ]

    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    # Mockの呼び出し回数を初期化
    event_publisher_mock.publish.call_count = 0
    auction_repository_mock.save.call_count = 0

    auction_events = auction_usecase.switch_auction()

    assert event_publisher_mock.publish.call_count == 0
    assert auction_repository_mock.save.call_count == 0
    assert auction_events == []


def test_正常系_オークション終了_イベント発行():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.OPEN
    START_DATETIME = datetime.now() - timedelta(days=2)
    END_DATETIME = datetime.now() - timedelta(days=1)
    auction_repository_mock.getAll.return_value = [
        Auction.reconstruct(
            id=ID,
            name=NAME,
            status=STATUS,
            start_datetime=START_DATETIME,
            end_datetime=END_DATETIME,
        )
    ]

    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    # Mockの呼び出し回数を初期化
    event_publisher_mock.publish.call_count = 0
    auction_repository_mock.save.call_count = 0

    auction_events = auction_usecase.switch_auction()

    assert event_publisher_mock.publish.call_count == 1
    assert auction_repository_mock.save.call_count == 1
    assert auction_events == [
        AuctionEvent(
            auction_id=ID,
            auction_name=NAME,
            type=Status.CLOSED,
        )
    ]


def test_正常系_オークション終了済み_イベント発行なし():
    ID = str(uuid.uuid4())
    NAME = "test_auction"
    STATUS = Status.CLOSED
    START_DATETIME = datetime.now() - timedelta(days=2)
    END_DATETIME = datetime.now() - timedelta(days=1)
    auction_repository_mock.getAll.return_value = [
        Auction.reconstruct(
            id=ID,
            name=NAME,
            status=STATUS,
            start_datetime=START_DATETIME,
            end_datetime=END_DATETIME,
        )
    ]

    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    # Mockの呼び出し回数を初期化
    event_publisher_mock.publish.call_count = 0
    auction_repository_mock.save.call_count = 0

    auction_events = auction_usecase.switch_auction()

    assert event_publisher_mock.publish.call_count == 0
    assert auction_repository_mock.save.call_count == 0
    assert auction_events == []
