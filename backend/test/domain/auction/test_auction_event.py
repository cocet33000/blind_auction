from main.domain.auction import AuctionEvent
from main.domain.auction.auction import Status


def test_auction_eventを作成():
    auction_id = "hoge"
    auction_name = "fuga"
    type = Status.CLOSED

    auction_event = AuctionEvent(
        auction_id=auction_id, auction_name=auction_name, type=type
    )

    assert auction_event.event_name == "AUCTION"
