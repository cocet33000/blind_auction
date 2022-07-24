from __future__ import annotations
import uuid

from . import dynamo_db
from main.domain.shared import EventPublisher
from main.domain.shared import Event
from main.domain.shared import DomainException


class EventPublisherImpl(EventPublisher):
    @staticmethod
    def publish(event: Event) -> dict:
        new_event = dynamo_db.Event(hash_key=str(uuid.uuid4()))
        new_event.name = event.event_name
        new_event.details = event.event_details

        try:
            new_event.save()
        except Exception as e:
            raise DomainException(e)
