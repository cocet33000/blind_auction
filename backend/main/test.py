from pathlib import Path
import sys

# add base project path to PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from main.usecase.item_usecase import ItemUseCase
from main.usecase.bid_usecase import BidUseCase

from main.domain.bid.bid_repository import BidRepository
from main.domain.item.item_repository import ItemRepository

from main.infrastructure.bid_repository_impl import BidRepositoryImpl
from main.infrastructure.item_repository_impl import ItemRepositoryImpl

from injector import Injector, Module, singleton, inject


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=BidRepositoryImpl)
        binder.bind(ItemRepository, to=ItemRepositoryImpl)


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
    print(bid_usecase.register_bid(user_name="fuga7", item_id=4, price=10000))
    print(bid_usecase.get_bids_by_user(user_name="hoge"))
