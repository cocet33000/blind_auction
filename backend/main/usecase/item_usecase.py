from injector import inject

from main.domain.item import ItemFactory
from main.domain.item import ItemRepository

from main.domain.auction import AuctionRepository


class ItemUseCase:
    @inject
    def __init__(
        self,
        ItemRepositoryImpl: ItemRepository,
        AuctionRepositoryImpl: AuctionRepository,
    ):
        self.ItemRepository = ItemRepositoryImpl
        self.AuctionRepository = AuctionRepositoryImpl

    def get_items(self) -> dict:
        items = self.ItemRepository.getAll()
        return {"items": [item.to_dict() for item in items]}

    def register_item(
        self,
        name: str,
        image_src: str,
        description: str,
        start_price: int,
        auction_id: str,
    ) -> dict:
        item_factory = ItemFactory(self.AuctionRepository)

        item = item_factory.create(
            name=name,
            image_src=image_src,
            description=description,
            start_price=start_price,
            auction_id=auction_id,
        )

        return self.ItemRepository.save(item)

    def get_items_by_auction_id(self, auction_id: str):
        return self.ItemRepository.getByAuctionId(auction_id)
