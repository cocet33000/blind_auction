from __future__ import annotations

from mock import Mock

from injector import Injector, Module, singleton

from main.domain.item import Item
from main.domain.item import Status as ItemStatus
from main.domain.value_object import Price
from main.domain.item import ItemRepository
from main.domain.auction import Status
from main.domain.auction import AuctionEvent
from main.domain.item.auction_event_subscriber import AuctionEventSubscriber


item_repository_mock = Mock(spec=ItemRepository)


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)


def test_正常系_1件_OPEN():
    target_item = Item.reconstruct(
        id="1",
        status=ItemStatus.BEFORE_AUCTION,
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id="uuid",
    )

    item_repository_mock.reset_mock()
    item_repository_mock.getByAuctionId.return_value = [target_item]
    item_repository_mock.save.return_value = None

    injector = Injector([DIModule()])
    auction_event_subscriber = injector.get(AuctionEventSubscriber)

    AUCTION_ID = "hoge"
    AUCTION_NAME = "fuga"
    TYPE = Status.OPEN

    auction_event = AuctionEvent(
        auction_id=AUCTION_ID, auction_name=AUCTION_NAME, type=TYPE
    )

    assert target_item.status == ItemStatus.BEFORE_AUCTION

    auction_event_subscriber.consume(auction_event)

    assert target_item.status == ItemStatus.UP_FOR_AUCTION

    assert item_repository_mock.getByAuctionId.call_count == 1
    assert item_repository_mock.save.call_count == 1


def test_正常系_2件_OPEN():
    target_item1 = Item.reconstruct(
        id="1",
        status=ItemStatus.BEFORE_AUCTION,
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id="uuid",
    )
    target_item2 = Item.reconstruct(
        id="2",
        status=ItemStatus.BEFORE_AUCTION,
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id="uuid",
    )

    item_repository_mock.reset_mock()
    item_repository_mock.getByAuctionId.return_value = [target_item1, target_item2]
    item_repository_mock.save.return_value = None

    injector = Injector([DIModule()])
    auction_event_subscriber = injector.get(AuctionEventSubscriber)

    AUCTION_ID = "hoge"
    AUCTION_NAME = "fuga"
    TYPE = Status.OPEN

    auction_event = AuctionEvent(
        auction_id=AUCTION_ID, auction_name=AUCTION_NAME, type=TYPE
    )

    assert target_item1.status == ItemStatus.BEFORE_AUCTION
    assert target_item2.status == ItemStatus.BEFORE_AUCTION

    auction_event_subscriber.consume(auction_event)

    assert target_item1.status == ItemStatus.UP_FOR_AUCTION
    assert target_item2.status == ItemStatus.UP_FOR_AUCTION

    assert item_repository_mock.getByAuctionId.call_count == 1
    assert item_repository_mock.save.call_count == 2


def test_正常系_1件_CLOSED():
    target_item = Item.reconstruct(
        id="1",
        status=ItemStatus.UP_FOR_AUCTION,
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id="uuid",
    )

    item_repository_mock.reset_mock()
    item_repository_mock.getByAuctionId.return_value = [target_item]
    item_repository_mock.save.return_value = None

    injector = Injector([DIModule()])
    auction_event_subscriber = injector.get(AuctionEventSubscriber)

    AUCTION_ID = "hoge"
    AUCTION_NAME = "fuga"
    TYPE = Status.CLOSED

    auction_event = AuctionEvent(
        auction_id=AUCTION_ID, auction_name=AUCTION_NAME, type=TYPE
    )

    assert target_item.status == ItemStatus.UP_FOR_AUCTION

    auction_event_subscriber.consume(auction_event)

    assert target_item.status == ItemStatus.SOLD_OUT

    assert item_repository_mock.getByAuctionId.call_count == 1
    assert item_repository_mock.save.call_count == 1


def test_正常系_2件_CLOSED():
    target_item1 = Item.reconstruct(
        id="1",
        status=ItemStatus.UP_FOR_AUCTION,
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id="uuid",
    )
    target_item2 = Item.reconstruct(
        id="2",
        status=ItemStatus.UP_FOR_AUCTION,
        name="hoge",
        image_src="test.png",
        description="hoge",
        start_price=Price(100),
        bid_num=0,
        auction_id="uuid",
    )

    item_repository_mock.reset_mock()
    item_repository_mock.getByAuctionId.return_value = [
        target_item1,
        target_item2,
    ]
    item_repository_mock.save.return_value = None

    injector = Injector([DIModule()])
    auction_event_subscriber = injector.get(AuctionEventSubscriber)

    AUCTION_ID = "hoge"
    AUCTION_NAME = "fuga"
    TYPE = Status.CLOSED

    auction_event = AuctionEvent(
        auction_id=AUCTION_ID, auction_name=AUCTION_NAME, type=TYPE
    )

    assert target_item1.status == ItemStatus.UP_FOR_AUCTION
    assert target_item2.status == ItemStatus.UP_FOR_AUCTION

    auction_event_subscriber.consume(auction_event)

    assert target_item1.status == ItemStatus.SOLD_OUT
    assert target_item2.status == ItemStatus.SOLD_OUT

    assert item_repository_mock.getByAuctionId.call_count == 1
    assert item_repository_mock.save.call_count == 2
