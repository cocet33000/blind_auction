from main.domain.shared.event import Event
from main.infrastructure.event_publisher_impl import EventPublisherImpl


def test_イベントをストアに格納できる():
    event = Event("test", {"test": "test"})
    EventPublisherImpl.publish(event)
