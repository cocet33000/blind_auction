from __future__ import annotations

from mock import Mock
from injector import Injector, Module, singleton

from main.domain.item import ItemRepository
from main.domain.auction import AuctionRepository

from main.usecase import ItemUseCase


item_repository_mock = Mock(spec=ItemRepository)

auction_repository_mock = Mock(spec=AuctionRepository)


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(ItemRepository, to=item_repository_mock)
        binder.bind(AuctionRepository, to=auction_repository_mock)


def test_正常系():
    injector = Injector([DIModule()])
    item_usecase = injector.get(ItemUseCase)
    auction_id = "1"

    item_usecase.get_items_by_auction_id(auction_id)

    assert item_repository_mock.getByAuctionId.call_count == 1
