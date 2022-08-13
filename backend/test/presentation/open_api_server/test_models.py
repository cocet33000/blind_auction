from main.presentation.openapi_server.models import BidHistoryBid


def test_モデルが読み込めるか確認する():
    bid_history_bid = BidHistoryBid(price=100, bided_at="2020-01-01T00:00:00+09:00")
    assert 100 == bid_history_bid.price
