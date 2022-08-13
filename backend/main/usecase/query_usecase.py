from __future__ import annotations
from abc import abstractmethod
from abc import ABC


class QueryUseCase(ABC):
    @staticmethod
    @abstractmethod
    def get_bid_history(user_name: str):
        raise NotImplementedError
