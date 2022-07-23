from __future__ import annotations
from abc import ABC
from abc import abstractmethod

from .event import Event


class EventSubscriber(ABC):
    @abstractmethod
    def consume(self, event: Event):
        raise NotImplementedError
