from __future__ import annotations
from abc import abstractmethod
from abc import ABC

from main.DomainModel.Bid import Bid
from main.DomainModel.BidsByUser import BidsByUser


class BidRepository(ABC):
    @staticmethod
    @abstractmethod
    def save(bid: Bid) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getByUserName(user_name: str) -> BidsByUser:
        raise NotImplementedError
