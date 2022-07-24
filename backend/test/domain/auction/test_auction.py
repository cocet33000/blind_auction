from main.domain.auction import Auction


def test_正常系_auctionインスタンスを生成():
    auction = Auction()
    assert auction is not None
