import uuid
from datetime import datetime

from main.domain.auction import Auction, Status
from main.infrastructure import AuctionRepositoryImpl


def test_正常系():
    auction_id = str(uuid.uuid4())

    # 保存
    auction = Auction.reconstruct(
        id=auction_id,
        name="auction01",
        status=Status.OPEN,
        start_datetime=datetime(2020, 1, 1),
        end_datetime=datetime(2020, 1, 1),
    )
    AuctionRepositoryImpl.save(auction)

    # 取得
    auction = AuctionRepositoryImpl.getById(auction_id)

    assert auction.to_dict()["id"] == auction_id
