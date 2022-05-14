from .BidRepository import BidRepository
from .ItemRepository import ItemRepository

from .BidRepositoryImpl import BidRepositoryImpl as BidRepositoryImplDynamoDB
from .ItemRepositoryImpl import ItemRepositoryImpl as ItemRepositoryImplDynamoDB

from injector import Injector, Module


class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=BidRepositoryImplDynamoDB)
        binder.bind(ItemRepository, to=ItemRepositoryImplDynamoDB)


injector = Injector([DIModule()])
BidRepositoryImpl: BidRepository = injector.get(BidRepository)
ItemRepositoryImpl: ItemRepository = injector.get(ItemRepository)

__all__ = ["BidRepositoryImpl", "ItemRepositoryImpl"]
