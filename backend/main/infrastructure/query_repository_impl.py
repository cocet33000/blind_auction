from __future__ import annotations
from main.domain.query import QueryRepository
from main.domain.query.bid_history import BidHistory


class QueryReositoryImpl(QueryRepository):
    @staticmethod
    def get_bid_history(user_id: str) -> BidHistory:
        # TODO: ここに実装する
        return None
