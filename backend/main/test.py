from pathlib import Path
import sys

# add base project path to PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from main.UseCase.ItemUseCase import ItemUseCase
from main.UseCase.BidUseCase import BidUseCase

from main.Infrastructure.BidRepository import BidRepository
from main.Infrastructure.ItemRepository import ItemRepository

from main.Infrastructure.BidRepositoryImpl import BidRepositoryImpl
from main.Infrastructure.ItemRepositoryImpl import ItemRepositoryImpl

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
    print(bid_usecase.register_bid(user_name="fuga3", item_id=4, price=10000))
    print(bid_usecase.get_bids_by_user(user_name="hoge"))
