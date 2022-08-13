from __future__ import annotations
from injector import inject

from main.domain.auction import AuctionRepository


class AuctionUseCase:
    @inject
    def __init__(
        self,
        AuctionRepositoryImpl: AuctionRepository,
    ):
        self.auction_repository = AuctionRepositoryImpl

    def get_auctions_all(self):
        auctions = self.auction_repository.getAll()
        return auctions
