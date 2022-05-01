from DynamoDBModel.Item import Item


class ItemRepository():
    def save(self, item):
        new_item = Item(hash(item))
        new_item.number = item.number
        new_item.name = item.name
        new_item.description = item.description
        new_item.start_price = item.start_price
        new_item.save()

        try:
            new_item.save()
            return "OK"
        except Exception as e:
            return "NG"

    def getByItemId(self, item_id):
        return Item.get(item_id)

    def getAll(self):
        return Item.scan()

    def deleteByItemId(self, item_id):
        item = Item(item_id)

        try:
            item.delete()
            return "OK"
        except Exception as e:
            return "NG"
