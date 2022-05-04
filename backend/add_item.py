import json

from Model.Item import Item
from Repository.ItemRepository import ItemRepository


def register_item(name: str, description: str, start_price: int):
    item = Item(
        name=name, description=description, start_price=start_price, bided_num=0
    )
    return ItemRepository.save(item)


if __name__ == "__main__":
    print(
        json.dumps(register_item(name="hoge", description="hoge hoge", start_price=100))
    )
