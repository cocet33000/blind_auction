from __future__ import annotations

from mock import Mock

from injector import Injector, Module, singleton

from main.domain.auction import AuctionRepository

from main.usecase import AuctionUseCase

auction_repository_mock = Mock(spec=AuctionRepository)


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(AuctionRepository, to=auction_repository_mock)


def test_正常系():
    auction_id = "hoge"

    injector = Injector([DIModule()])
    auction_usecase = injector.get(AuctionUseCase)

    auction_event = auction_usecase.switch_auction(auction_id)

    assert auction_event.get("id") == auction_id
    assert auction_event.get("status") == "OPEN"
