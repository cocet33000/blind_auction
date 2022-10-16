from __future__ import annotations

import uuid
import pytest
from mock import Mock
import datetime

from injector import Injector, Module, singleton

from main.domain.value_object import Price
from main.domain.item import ItemRepository
from main.domain.item import Item
from main.domain.item import Status
from main.domain.bid import Bid
from main.domain.bid import AllBidsByUser
from main.domain.bid import BidRepository
from main.domain.shared import EventPublisher
from main.usecase import BidUseCase
from main.usecase import BidAlreadyExistsError

START_PRICE = 500
item_repository_mock = Mock(spec=ItemRepository)
item_repository_mock.getByItemId.return_value = Item.reconstruct(
    id="1",
    status=Status.BEFORE_AUCTION,
    name="fuga",
    image_src="test.png",
    description="fuga",
    start_price=Price(START_PRICE),
    bid_num=0,
    auction_id=str(uuid.uuid4()),
)
bid_repository_mock = Mock(spec=BidRepository)
bid_repository_mock.getByUserName.return_value = AllBidsByUser(
    [
        Bid.reconstruct(
            id="bid" + str(uuid.uuid4()),
            bided_user_name="hoge",
            bid_item_id="2",
            price=Price(1000),
            bided_at=datetime.datetime.now(),
        )
    ]
)
bid_repository_mock.save.return_value = {"is_error": False}

event_publisher_mock = Mock(spec=EventPublisher)
event_publisher_mock.publish.return_value = {"is_error": False}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=bid_repository_mock)
        binder.bind(ItemRepository, to=item_repository_mock)
        binder.bind(EventPublisher, to=event_publisher_mock)


def test_正常系():
    injector = Injector([DIModule()])
    bid_usecase = injector.get(BidUseCase)

    test_user_name = "hoge"
    test_item_id = "1"
    test_price = 1000

    bid_usecase.register_bid(test_user_name, test_item_id, test_price)
    assert event_publisher_mock.publish.call_count == 1


def test_既に入札済みのユーザーの場合は例外を投げる():
    injector = Injector([DIModule()])
    bid_usecase = injector.get(BidUseCase)

    test_user_name = "hoge"
    test_item_id = "2"
    test_price = 1000

    # 既に入札済みのユーザーの場合は例外を投げる
    with pytest.raises(BidAlreadyExistsError):
        bid_usecase.register_bid(test_user_name, test_item_id, test_price)
