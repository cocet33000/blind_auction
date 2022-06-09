from injector import inject
import datetime

from main.DomainModel.Bid import Bid
from main.DomainModel.Item import Item
from main.Infrastructure.ItemRepository import ItemRepository
from main.Infrastructure.BidRepository import BidRepository


class BidUseCase:
    @inject
    def __init__(
        self, ItemRepositoryImpl: ItemRepository, BidRepositoryImpl: BidRepository
    ):
        self.ItemRepository = ItemRepositoryImpl
        self.BidRepository = BidRepositoryImpl

    def register_bid(self, user_name: str, item_id: int, price: int) -> dict:
        bids_by_user = self.BidRepository.getByUserName(user_name)
        if bids_by_user.exists_bid_by_item_id(item_id):
            raise BidAlreadyExistsError

        bid = Bid(
            bided_user_name=user_name,
            bid_item_id=item_id,
            bided_at=datetime.datetime.now(),
            price=price,
        )
        return self.BidRepository.save(bid)

    # getByUserNameの戻り値を変更（list(Bid) -> BidsByUser）したので動かない
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


class BidAlreadyExistsError(Exception):
    pass
