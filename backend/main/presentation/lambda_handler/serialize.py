from ..openapi_server.models.bid_historys import BidHistorys
from ..openapi_server.models.bid_history import BidHistory
from ..openapi_server.models.bid_history_bid import BidHistoryBid
from ..openapi_server.models.bid_history_item import BidHistoryItem


def bids_history_serialize(bid_historys: list):
    return BidHistorys(
        bid_historys=[
            BidHistory(
                item=BidHistoryItem(
                    id=bid_history["item"]["id"],
                    name=bid_history["item"]["name"],
                    image_src=bid_history["item"]["image_src"],
                    description=bid_history["item"]["description"],
                    start_price=bid_history["item"]["start_price"],
                ),
                bid=BidHistoryBid(
                    price=bid_history["bid"]["price"],
                    bided_at=bid_history["bid"]["bided_at"].isoformat(),
                ),
            )
            for bid_history in bid_historys
        ]
    ).to_dict()
