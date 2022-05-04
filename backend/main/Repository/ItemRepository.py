from DynamoDBModel.Item import Item as DynamoDBItem
from DynamoDBModel.Sequence import Sequence as DynamoDBSequene
from Model.Item import Item


class ItemRepository:
    @staticmethod
    def save(item: Item) -> dict:
        def getNewId():
            sequence = DynamoDBSequene("items")
            sequence.update(actions=[DynamoDBSequene.current_number.add(1)])
            return sequence.current_number

        new_id = getNewId()
        new_item = DynamoDBItem(new_id)
        new_item.name = item.name
        new_item.image_src = item.image_src
        new_item.description = item.description
        new_item.start_price = item.start_price
        new_item.save()

        try:
            new_item.save()
            return {"is_error": False, "id": new_id}
        except Exception as e:
            return {"is_error": True}

    @staticmethod
    def getByItemId(item_id):
        return DynamoDBItem.get(item_id)

    @staticmethod
    def getAll():
        return DynamoDBItem.scan()

    @staticmethod
    def deleteByItemId(item_id):
        item = DynamoDBItem(item_id)

        try:
            item.delete()
            return "OK"
        except Exception as e:
            return "NG"
