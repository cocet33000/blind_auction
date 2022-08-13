from __future__ import annotations

from . import dynamo_db
from main.domain.auction import Auction

from main.domain.auction import AuctionRepository
from main.domain.shared import DomainException


class AuctionRepositoryImpl(AuctionRepository):
    @staticmethod
    def save(auction) -> dict:
        _auction = auction.to_dict()

        new_auction = dynamo_db.Auction(hash_key=_auction["id"], range_key="auction")
        new_auction.name = _auction["name"]
        new_auction.status = _auction["status"]
        new_auction.start_datetime = _auction["start_datetime"]
        new_auction.end_datetime = _auction["end_datetime"]
        new_auction.save()

        try:
            new_auction.save()
        except Exception as e:
            raise DomainException(e)

    @staticmethod
    def getAll():
        return []
