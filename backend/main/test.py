from UseCase import ItemUseCase
from UseCase import BidUseCase

from Infrastructure import BidRepository
from Infrastructure import ItemRepository

from Infrastructure import BidRepositoryImplDynamoDB
from Infrastructure import ItemRepositoryImplDynamoDB

from injector import Injector, Module, singleton, inject


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=BidRepositoryImplDynamoDB)
        binder.bind(ItemRepository, to=ItemRepositoryImplDynamoDB)


if __name__ == "__main__":
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)
    bid_usecase = injector.get(BidUseCase)
    print(item_usecase.get_items())
    print(
        item_usecase.register_item(
            name="hoge",
            image_src="http://test",
            description="hoge hoge",
            start_price=100,
        )
    )
    print(bid_usecase.register_bid(user_name="fuga", item_id=4, price=10000))
    print(bid_usecase.get_bids_by_user(user_name="hoge"))
