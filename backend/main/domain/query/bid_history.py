from __future__ import annotations


class BidHistory:
    """あるユーザーの入札履歴

    Args:

    """

    def __init__(self, user_id, bid_history):
        self._user_id = user_id
        self._bid_history = bid_history

    def get_user_id(self):
        return self._user_id
