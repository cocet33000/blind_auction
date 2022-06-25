from injector import inject

from main.domain.item import ItemFactory
from main.domain.item import ItemRepository


class ItemUseCase:
    @inject
    def __init__(self, ItemRepositoryImpl: ItemRepository):
        self.ItemRepository = ItemRepositoryImpl

    def get_items(self) -> dict:
        items = self.ItemRepository.getAll()
        return {"items": [item.to_dict() for item in items]}

    def register_item(
        self, name: str, image_src: str, description: str, start_price: int
    ) -> dict:
        item = ItemFactory.create(
            name=name,
            image_src=image_src,
            description=description,
            start_price=start_price,
        )

        return self.ItemRepository.save(item)
