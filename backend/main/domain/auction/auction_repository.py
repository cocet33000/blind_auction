from __future__ import annotations
from abc import ABC
from abc import abstractmethod

from .auction import Auction


class AuctionRepository(ABC):
    @staticmethod
    @abstractmethod
    def save(item: Auction) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getAll() -> list[Auction]:
        raise NotImplementedError
