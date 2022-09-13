from __future__ import annotations
from injector import inject
from datetime import datetime, timedelta, timezone

from main.domain.auction import AuctionFactory
from main.domain.auction import AuctionRepository
from main.domain.shared import EventPublisher

import logging


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

    def switch_auction(self):
        auctions = self.get_auctions_all()
        events = []
        try:
            for auction in auctions:
                auction_event = auction.switchStatus(
                    now_datetime=datetime.now(timezone(timedelta(hours=9)))
                )
                if auction_event is not None:
                    events.append(auction_event)
                    self.auction_repository.save(auction)
                    self.EventPublisher.publish(auction_event)
            return events
        except Exception:
            logging.exception("")
            return {}
