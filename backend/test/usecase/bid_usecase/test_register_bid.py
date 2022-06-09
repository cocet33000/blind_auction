from __future__ import annotations

import unittest
from mock import Mock
import datetime

from injector import Injector, Module, singleton

from main.domain.bid.bid_repository import BidRepository
from main.domain.item.item_repository import ItemRepository
from main.domain.value_object.price import Price
from main.domain.bid.bid import Bid
from main.domain.bid.bids_by_user import BidsByUser
from main.usecase.bid_usecase import BidUseCase
from main.usecase.bid_usecase import BidAlreadyExistsError

item_repository_mock = Mock(spec=ItemRepository)
bid_repository_mock = Mock(spec=BidRepository)
bid_repository_mock.getByUserName.return_value = BidsByUser(
    [
        Bid(
            bided_user_name="hoge",
            bid_item_id=2,
            price=Price(1000),
            bided_at=datetime.datetime.now(),
        )
    ]
)
bid_repository_mock.save.return_value = {"is_error": False}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=bid_repository_mock)
        binder.bind(ItemRepository, to=item_repository_mock)


class TestRegisterBid(unittest.TestCase):
    def test_正常系(self):
        injector = Injector([DIModule()])
        bid_usecase = injector.get(BidUseCase)

        test_user_name = "hoge"
        test_item_id = 1
        test_price = 1000

        response = bid_usecase.register_bid(test_user_name, test_item_id, test_price)

        self.assertEqual(response["is_error"], False)

    def test_既に入札済みのユーザーの場合は例外を投げる(self):
        injector = Injector([DIModule()])
        bid_usecase = injector.get(BidUseCase)

        test_user_name = "hoge"
        test_item_id = 2
        test_price = 1000

        # 既に入札済みのユーザーの場合は例外を投げる
        with self.assertRaises(BidAlreadyExistsError):
            bid_usecase.register_bid(test_user_name, test_item_id, test_price)
