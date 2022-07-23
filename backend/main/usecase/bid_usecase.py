from injector import inject

from main.domain.item import Item
from main.domain.item import ItemRepository
from main.domain.bid import BidRepository
from main.domain.bid import BidFactory
from main.domain.bid import BidEvent
from main.domain.shared import EventPublisher


class BidUseCase:
    @inject
    def __init__(
        self,
        ItemRepositoryImpl: ItemRepository,
        BidRepositoryImpl: BidRepository,
        EventPublisherImpl: EventPublisher,
    ):
        self.ItemRepository = ItemRepositoryImpl
        self.BidRepository = BidRepositoryImpl
        self.EventPublisher = EventPublisherImpl

    def register_bid(self, user_name: str, item_id: str, price: int) -> dict:
        # 同一ユーザーは同一商品に一度しか入札できない
        # この知識はユースケースではなく、ドメインに持たせても良いかもしれない
        bids_by_user = self.BidRepository.getByUserName(user_name)
        if bids_by_user.exists_bid_by_item_id(item_id):
            raise BidAlreadyExistsError

        bid_factory = BidFactory(self.ItemRepository)
        bid = bid_factory.create(
            user_name,
            item_id,
            price,
        )

        # WARNING: 本来はRepositoryへの永続化とEventの発行は同一トランザクションで行う必要がある
        res = self.BidRepository.save(bid)
        # TODO: dictを返すのではなくエラーをraiseするようにする
        if res.get("is_error"):
            return {"is_error": True}

        bid_event = BidEvent(user_name, item_id, price)
        res = self.EventPublisher.publish(bid_event)
        if res.get("is_error"):
            # TODO: dictを返すのではなくエラーをraiseするようにする
            return {"is_error": True}

        return {"is_error": False}

    # getByUserNameの戻り値を変更（list(Bid) -> AllBidsByUser）したので動かない
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
