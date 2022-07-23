from __future__ import annotations
from abc import ABC
from abc import abstractmethod

from .event import Event


class EventPublisher(ABC):
    @staticmethod
    @abstractmethod
    def publish(event: Event):
        raise NotImplementedError
