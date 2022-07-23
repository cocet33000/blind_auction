from main.domain.bid.bid_event import BidEvent


def test_bid_eventを作成():
    user_name = "hoge"
    item_id = "1"
    price = 100

    bid_event = BidEvent(user_name, item_id, price)

    assert bid_event.event_name == "BID"
    assert bid_event.user_name() == user_name
    assert bid_event.item_id() == item_id
    assert bid_event.price() == price
