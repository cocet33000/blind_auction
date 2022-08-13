import uuid
from datetime import datetime

from main.domain.auction import Auction, Status
from main.infrastructure.auction_repository_impl import AuctionRepositoryImpl


def test_正常系():
    auction = Auction.reconstruct(
        id=str(uuid.uuid4()),
        name="auction01",
        status=Status.OPEN,
        start_datetime=datetime(2020, 1, 1),
        end_datetime=datetime(2020, 1, 1),
    )
    res = AuctionRepositoryImpl.save(auction)
