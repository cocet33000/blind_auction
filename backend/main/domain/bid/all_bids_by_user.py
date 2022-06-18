from __future__ import annotations

from .bid import Bid


class AllBidsByUser(list):
    """あるユーザーの全ての入札

    Args:
        bids: list[Bid]

    """

    _bids = []

    def __init__(self, bids: list[Bid]):
        self._bids = bids

    def exists_bid_by_item_id(self, item_id: str) -> bool:
        for bid_by_user in self._bids:
            if bid_by_user.bid_item_id == item_id:
                return True

        return False
