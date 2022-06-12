from __future__ import annotations
import logging


from . import dynamo_db
from main.domain.item import Item
from main.domain.item import ItemRepository


class ItemRepositoryImpl(ItemRepository):
    @staticmethod
    def save(item: Item) -> dict:
        new_item = dynamo_db.Item(item.id)
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
        return dynamo_db.Item.get(item_id).to_model()

    @staticmethod
    def getAll() -> list[Item]:
        return [item.to_model() for item in dynamo_db.Item.scan()]

    @staticmethod
    def deleteByItemId(item_id):
        item = dynamo_db.Item(item_id)

        try:
            item.delete()
            return "OK"
        except Exception as e:
            logging.error(e)
            return "NG"