from __future__ import annotations

from ..shared import Event


class BidEvent(Event):
    def __init__(self, user_name: str, item_id: str, price: int) -> None:
        event_name = "BID"
        event_details = {
            "user_name": user_name,
            "item_id": item_id,
            "price": price,
        }
        super().__init__(event_name, event_details)

    def user_name(self):
        return self.event_details.get("user_name")

    def item_id(self):
        return self.event_details.get("item_id")

    def price(self):
        return self.event_details.get("price")
