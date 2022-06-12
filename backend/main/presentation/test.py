from usecase import ItemUseCase
from usecase import BidUseCase

from domain.bid import BidRepository
from domain.item import ItemRepository

from infrastructure import BidRepositoryImpl
from infrastructure import ItemRepositoryImpl

from injector import Injector, Module, singleton


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=BidRepositoryImpl)
        binder.bind(ItemRepository, to=ItemRepositoryImpl)


injector = Injector([DIModule()])
item_usecase = injector.get(ItemUseCase)
bid_usecase = injector.get(BidUseCase)
print(item_usecase.get_items())
# print(
#     item_usecase.register_item(
#         name="hoge",
#         image_src="http://test",
#         description="hoge hoge",
#         start_price=100,
#     )
# )
# print(bid_usecase.register_bid(user_name="fuga7", item_id=4, price=10000))
print(bid_usecase.get_bids_by_user(user_name="hoge"))
