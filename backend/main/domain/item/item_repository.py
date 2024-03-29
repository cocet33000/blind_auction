from __future__ import annotations
from abc import ABC
from abc import abstractmethod

from .item import Item


class ItemRepository(ABC):
    @staticmethod
    @abstractmethod
    def save(item: Item) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def bidNumIncrement(item_id: str) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getByItemId(item_id):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getByAuctionId(auction_id):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getAll() -> list[Item]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def deleteByItemId(item_id):
        raise NotImplementedError
