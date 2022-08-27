from __future__ import annotations

from ..shared import Event
from .auction import Status


class AuctionEvent(Event):
    def __init__(self, auction_id, type: Status) -> None:
        event_name = "AUCTION"
        event_details = {
            "auction_id": auction_id,
            "type": type,
        }
        super().__init__(event_name, event_details)

    def auction_id(self):
        return self.event_details.get("auction_id")

    def type(self):
        return self.event_details.get("type")
