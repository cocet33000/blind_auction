from __future__ import annotations
import logging
import uuid

from . import dynamo_db
from main.domain.shared import EventPublisher
from main.domain.shared import Event


class EventPublisherImpl(EventPublisher):
    @staticmethod
    def publish(event: Event) -> dict:
        new_event = dynamo_db.Event(hash_key=str(uuid.uuid4()))
        new_event.name = event.event_name
        new_event.details = event.event_details

        try:
            new_event.save()
            return {"is_error": False}
        except Exception as e:
            logging.error(e)
            return {"is_error": True}
