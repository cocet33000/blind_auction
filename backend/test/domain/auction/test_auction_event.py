from main.domain.auction.auction_event import AuctionEvent
from main.domain.auction.auction import Status


def test_auction_eventを作成():
    auction_id = "hoge"
    type = Status.CLOSED

    auction_event = AuctionEvent(auction_id=auction_id, type=type)

    assert auction_event.event_name == "AUCTION"
