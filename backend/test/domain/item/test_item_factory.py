import pytest

from mock import Mock

from main.domain.shared import DomainException
from main.domain.item import ItemFactory
from main.domain.auction import AuctionRepository

auction_repository_mock = Mock(spec=AuctionRepository)


def test_itemを生成():
    auction_repository_mock.getById.return_value = None
    item_factory = ItemFactory(auction_repository_mock)

    item = item_factory.create("hoge", "hoge", "hoge", 100, "uuid")

    assert item.id is not None
    assert item.name == "hoge"
    assert item.image_src == "hoge"
    assert item.description == "hoge"
    assert item.start_price == 100
    assert item.bid_num == 0
    assert item.auction_id == "uuid"


# def test_存在しないオークションID():
#     auction_repository_mock.getById.side_effect = DomainException("")

#     item_factory = ItemFactory(auction_repository_mock)

#     with pytest.raises(DomainException):
#         item_factory.create("hoge", "hoge", "hoge", 100, "not_exist_uuid")
