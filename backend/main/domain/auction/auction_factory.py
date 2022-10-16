import uuid
from injector import inject

from main.domain.shared.errors.errors import DomainException


from .auction import Auction, Period
from .auction import Status
from .auction_repository import AuctionRepository


class AuctionFactory:
    @inject
    def __init__(self, AuctionRepositoryImpl: AuctionRepository):
        self.auction_repository = AuctionRepositoryImpl

    def create(self, name: str, start_datetime, end_datetime) -> Auction:
        # TODO: 現在時刻より早いstart_datetimeはエラーを実装

        existing_auctions = self.auction_repository.getAll()
        period = Period(start_datetime, end_datetime)

        if exists_same_period_auction(period, existing_auctions):
            raise DomainException

        def getNewId() -> str:
            return "auction" + str(uuid.uuid4())

        new_id = getNewId()
        return Auction(
            id=new_id,
            name=name,
            status=Status.CLOSED,
            period=period,
        )


def exists_same_period_auction(period, existing_auctions):
    for existing_auction in existing_auctions:
        if (
            existing_auction.start_datetime()
            <= period.start_datetime
            <= existing_auction.end_datetime()
            or existing_auction.start_datetime()
            <= period.end_datetime
            <= existing_auction.end_datetime()
        ):
            return True

    return False
