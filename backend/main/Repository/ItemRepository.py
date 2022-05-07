from __future__ import annotations
import logging

from . import DynamoDBModel
import DomainModel


class ItemRepository:
    @staticmethod
    def save(item: DomainModel.Item) -> dict:
        new_item = DynamoDBModel.Item(item.id)
        new_item.name = item.name
        new_item.image_src = item.image_src
        new_item.description = item.description
        new_item.start_price = item.start_price
        new_item.save()

        try:
            new_item.save()
            return {"is_error": False, "id": item.id}
        except Exception as e:
            logging.error(e)
            return {"is_error": True}

    @staticmethod
    def getByItemId(item_id):
        return DynamoDBModel.Item.get(item_id)

    @staticmethod
    def getAll() -> list[DomainModel.Item]:
        return [item.to_model() for item in DynamoDBModel.Item.scan()]

    @staticmethod
    def deleteByItemId(item_id):
        item = DynamoDBModel.Item(item_id)

        try:
            item.delete()
            return "OK"
        except Exception as e:
            logging.error(e)
            return "NG"
