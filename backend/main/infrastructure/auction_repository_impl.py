from __future__ import annotations

from . import dynamo_db
from main.domain.auction import Auction

from main.domain.auction import AuctionRepository
from main.domain.shared import DomainException


class AuctionRepositoryImpl(AuctionRepository):
    @staticmethod
    def save(auction) -> dict:
        _auction = auction.to_dict()

        new_auction = dynamo_db.Auction(hash_key="auction", range_key=_auction["id"])
        new_auction.auction_name = _auction["name"]
        new_auction.auction_status = _auction["status"]
        new_auction.auction_start_datetime = _auction["start_datetime"]
        new_auction.auction_end_datetime = _auction["end_datetime"]
        new_auction.save()

        try:
            new_auction.save()
        except Exception as e:
            raise DomainException(e)

    @staticmethod
    def getAll():
        return [
            auction.to_model()
            for auction in dynamo_db.Auction.query(hash_key="auction")
        ]

    @staticmethod
    def getById(id):
        return dynamo_db.Auction.get(hash_key="auction", range_key=id).to_model()
