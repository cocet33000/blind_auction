from __future__ import annotations
from injector import inject
from datetime import datetime

from main.domain.auction import AuctionFactory
from main.domain.auction import AuctionEvent
from main.domain.auction import AuctionRepository
from main.domain.auction.auction import Status
from main.domain.shared import EventPublisher


class AuctionUseCase:
    @inject
    def __init__(
        self,
        AuctionRepositoryImpl: AuctionRepository,
        EventPublisherImpl: EventPublisher,
    ):
        self.auction_repository = AuctionRepositoryImpl
        self.EventPublisher = EventPublisherImpl

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
            auction.switchStatus(now_datetime=datetime.now())
            _auction = auction.to_dict()
            # auction_event = {
            #     "id": _auction.get("id"),
            #     "name": _auction.get("name"),
            #     "status": "OPEN",
            # }
            auction_event = AuctionEvent(
                auction_id=auction_id,
                auction_name=_auction.get("name"),
                type=Status.OPEN,
            )

            self.auction_repository.save(auction)
            self.EventPublisher.publish(auction_event)
            return auction_event
        except Exception as e:
            return {}
