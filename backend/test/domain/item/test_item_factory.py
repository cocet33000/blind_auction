from mock import Mock

from main.domain.item import ItemFactory
from main.domain.auction import AuctionRepository

auction_repository_mock = Mock(spec=AuctionRepository)


def test_itemを生成():
    item_factory = ItemFactory(auction_repository_mock)

    item = item_factory.create("hoge", "hoge", "hoge", 100, "uuid")

    assert item.id is not None
    assert item.name == "hoge"
    assert item.image_src == "hoge"
    assert item.description == "hoge"
    assert item.start_price == 100
    assert item.bid_num == 0
    assert item.auction_id == "uuid"
