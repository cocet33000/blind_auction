from __future__ import annotations
import uuid

from . import dynamo_db
from main.domain.shared import EventPublisher
from main.domain.shared import Event
from main.domain.shared import DomainException


class EventPublisherImpl(EventPublisher):
    @staticmethod
    def publish(event: Event) -> None:
        new_event = dynamo_db.Event(hash_key=str(uuid.uuid4()))
        new_event.name = event.event_name
        # PynamoDBのEventがEnumをsave出来ないため、文字列に変換
        new_event.details = {
            "auction_id": event.event_details["auction_id"],
            "name": event.event_details["name"],
            "type": event.event_details["type"].value,
        }

        try:
            new_event.save()
        except Exception as e:
            raise DomainException(e)
