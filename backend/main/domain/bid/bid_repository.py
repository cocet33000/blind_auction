from __future__ import annotations
from abc import abstractmethod
from abc import ABC

from .bid import Bid
from .bids_by_user import BidsByUser


class BidRepository(ABC):
    @staticmethod
    @abstractmethod
    def save(bid: Bid) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getByUserName(user_name: str) -> BidsByUser:
        raise NotImplementedError
