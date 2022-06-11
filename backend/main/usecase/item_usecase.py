from injector import inject

from domain.item.item_factory import ItemFactory
from domain.item.item_repository import ItemRepository


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
        item = ItemFactory.Create(
            name=name,
            image_src=image_src,
            description=description,
            start_price=start_price,
        )

        return self.ItemRepository.save(item)
