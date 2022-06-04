from __future__ import annotations
from abc import abstractmethod
from abc import ABC

import DomainModel


class BidRepository(ABC):
    @staticmethod
    @abstractmethod
    def save(bid: DomainModel.Bid) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getByUserName(user_name: str) -> DomainModel.BidsByUser:
        raise NotImplementedError
