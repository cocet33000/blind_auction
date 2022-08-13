from __future__ import annotations
from injector import inject
from datetime import datetime

from main.domain.auction import AuctionFactory
from main.domain.auction import AuctionRepository


class AuctionUseCase:
    @inject
    def __init__(
        self,
        AuctionRepositoryImpl: AuctionRepository,
    ):
        self.auction_repository = AuctionRepositoryImpl

    def register_auction(
        self,
        name: str,
        start_datetime: datetime,
        end_datetime: datetime,
    ):
        auction = AuctionFactory.create(name, start_datetime, end_datetime)
        self.auction_repository.save(auction)

    def get_auctions_all(self):
        auctions = self.auction_repository.getAll()
        return auctions
