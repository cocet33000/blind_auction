from __future__ import annotations

import uuid
import pytest

from mock import Mock
import datetime

from injector import Injector, Module, singleton

from main.domain.auction import AuctionRepository
from main.domain.auction.auction_factory import AuctionFactory
from main.domain.shared.event.event_publisher import EventPublisher

from main.usecase.auction_usecase import AuctionUseCase

auction_factory_mock = Mock(spec=AuctionFactory)
auction_repository_mock = Mock(spec=AuctionRepository)

event_publisher_mock = Mock(spec=EventPublisher)
event_publisher_mock.publish.return_value = {"is_error": False}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(AuctionFactory, to=auction_factory_mock)
        binder.bind(AuctionRepository, to=auction_repository_mock)
        binder.bind(EventPublisher, to=event_publisher_mock)


def test_正常系():
    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    auction_usecase.register_auction(
        name="1",
        start_datetime=datetime.datetime.now(),
        end_datetime=datetime.datetime.now(),
    )

    assert auction_factory_mock.create.call_count == 1
    assert auction_repository_mock.save.call_count == 1
