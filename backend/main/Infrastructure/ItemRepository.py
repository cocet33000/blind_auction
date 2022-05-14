from __future__ import annotations
from abc import ABC
from abc import abstractmethod

import DomainModel


class ItemRepository(ABC):
    @staticmethod
    @abstractmethod
    def save(item: DomainModel.Item) -> dict:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getByItemId(item_id):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def getAll() -> list[DomainModel.Item]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def deleteByItemId(item_id):
        raise NotImplementedError
