from injector import inject
import datetime

from DomainModel import Bid
from DomainModel import Item
from Infrastructure import ItemRepository
from Infrastructure import BidRepository


class BidUseCase:
    @inject
    def __init__(
        self, ItemRepositoryImpl: ItemRepository, BidRepositoryImpl: BidRepository
    ):
        self.ItemRepository = ItemRepositoryImpl
        self.BidRepository = BidRepositoryImpl

    def register_bid(self, user_name: str, item_id: int, price: int) -> dict:
        bid = Bid(
            bided_user_name=user_name,
            bid_item_id=item_id,
            bided_at=datetime.datetime.now(),
            price=price,
        )
        return self.BidRepository.save(bid)

    def get_bids_by_user(self, user_name: str) -> dict:
        bids = self.BidRepository.getByUserName(user_name)

        # 可読性と再利用性のために、N+1クエリを許容しているが、必要に応じてリファクタリングする
        items: list[Item] = [
            self.ItemRepository.getByItemId(bid.bid_item_id) for bid in bids
        ]

        return {
            "bids": [bid.to_dict() for bid in bids],
            "items": [item.to_dict() for item in items],
        }
