from __future__ import annotations
from abc import abstractmethod
from abc import ABC

from .bid_history import BidHistory


class QueryRepository(ABC):
    @staticmethod
    @abstractmethod
    def get_bid_history(user_id: str) -> BidHistory:
        raise NotImplementedError
