from main.domain.auction import AuctionEvent
from main.domain.auction import Status
from main.domain.shared.event import Event
from main.infrastructure.event_publisher_impl import EventPublisherImpl


def test_イベントをストアに格納できる():
    event = Event("test", {"test": "test"})
    EventPublisherImpl.publish(event)


def test_AuctionEventをストアに格納できる():
    event = AuctionEvent(auction_id="hoge", auction_name="fuga", type=Status.CLOSED)
    EventPublisherImpl.publish(event)
