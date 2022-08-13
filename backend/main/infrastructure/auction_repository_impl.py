from __future__ import annotations

from main.domain.auction import AuctionRepository


class AuctionRepositoryImpl(AuctionRepository):
    @staticmethod
    def save() -> dict:
        return {}

    @staticmethod
    def getAll():
        return []
