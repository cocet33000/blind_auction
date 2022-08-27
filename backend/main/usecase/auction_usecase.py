from __future__ import annotations
from unicodedata import name
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

    def switch_auction(self, auction_id):
        auction = self.auction_repository.getById(auction_id)
        try:
            # auction_event = auction.switch()
            auction_event = {"id": auction_id, "name": "auction_name", "status": "OPEN"}
            return auction_event
        except Exception as e:
            return {}
