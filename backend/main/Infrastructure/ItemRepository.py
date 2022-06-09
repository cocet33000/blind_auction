from __future__ import annotations
from abc import ABC
from abc import abstractmethod

from main.DomainModel.Item import Item


class ItemRepository(ABC):
    @staticmethod
    @abstractmethod
    def save(item: Item) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getByItemId(item_id):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getAll() -> list[Item]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def deleteByItemId(item_id):
        raise NotImplementedError
