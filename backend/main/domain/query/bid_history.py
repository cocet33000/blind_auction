from __future__ import annotations


class BidHistory:
    """あるユーザーの入札履歴

    Args:

    """

    def __init__(self, user_name, bid_history):
        self._user_name = user_name
        self._bid_history = bid_history

    def get_user_name(self):
        return self._user_name
