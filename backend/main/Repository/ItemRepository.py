import logging

import DynamoDBModel
import Model


class ItemRepository:
    @staticmethod
    def save(item: Model.Item) -> dict:
        def getNewId():
            sequence = DynamoDBModel.Sequence("items")
            sequence.update(actions=[DynamoDBModel.Sequence.current_number.add(1)])
            return sequence.current_number

        new_id = getNewId()
        new_item = DynamoDBModel.Item(new_id)
        new_item.name = item.name
        new_item.image_src = item.image_src
        new_item.description = item.description
        new_item.start_price = item.start_price
        new_item.save()

        try:
            new_item.save()
            return {"is_error": False, "id": new_id}
        except Exception as e:
            logging.error(e)
            return {"is_error": True}

    @staticmethod
    def getByItemId(item_id):
        return DynamoDBModel.Item.get(item_id)

    @staticmethod
    def getAll():
        return DynamoDBModel.Item.scan()

    @staticmethod
    def deleteByItemId(item_id):
        item = DynamoDBModel.Item(item_id)

        try:
            item.delete()
            return "OK"
        except Exception as e:
            logging.error(e)
            return "NG"
