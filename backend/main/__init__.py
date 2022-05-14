from Infrastructure import BidRepository
from Infrastructure import ItemRepository

from Infrastructure import BidRepositoryImplDynamoDB
from Infrastructure import ItemRepositoryImplDynamoDB

from injector import Module


class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=BidRepositoryImplDynamoDB)
        binder.bind(ItemRepository, to=ItemRepositoryImplDynamoDB)


__all__ = ["DIModule"]
