import json

from DomainService import ItemFactory
from Infrastructure import ItemRepositoryImpl


def register_item(
    name: str, image_src: str, description: str, start_price: int
) -> dict:
    item = ItemFactory.Create(
        name=name,
        image_src=image_src,
        description=description,
        start_price=start_price,
    )

    return ItemRepositoryImpl.save(item)


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
