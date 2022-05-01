from Model.Item import Item
from Repository.ItemRepository import ItemRepository

if __name__ == "__main__":
    item = Item(
        number=100,
        name="fuga",
        description="fugaです。",
        start_price=100,
        bided_num=0
    )
    item_repository = ItemRepository()
    item_repository.save(item)

