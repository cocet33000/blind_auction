from __future__ import annotations
from abc import ABC
from dataclasses import dataclass


@dataclass
class Event(ABC):
    """Eventの基底クラス"""

    def __init__(self, event_name: str, event_details: dict) -> None:
        self.event_name = event_name
        self.event_details = event_details
