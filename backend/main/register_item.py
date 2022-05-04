import json

from Model.Item import Item
from Repository.ItemRepository import ItemRepository


def register_item(name: str, image_src: str, description: str, start_price: int):
    item = Item(
        name=name,
        image_src=image_src,
        description=description,
        start_price=start_price,
        bid_num=0,
    )
    return ItemRepository.save(item)


if __name__ == "__main__":
    print(
        json.dumps(
            register_item(
                name="hoge",
                image_src="http://test",
                description="hoge hoge",
                start_price=100,
            )
        )
    )
