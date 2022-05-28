from __future__ import annotations

import unittest
from mock import Mock
import datetime
from pathlib import Path
import sys

from injector import Injector, Module, singleton, inject

sys.path.append(str(Path(__file__).parent.parent.parent / "main"))
from Infrastructure import BidRepository, ItemRepository
import DomainModel
from UseCase import BidUseCase

item_repository_mock = Mock(spec=ItemRepository)
bid_repository_mock = Mock(spec=BidRepository)
bid_repository_mock.getByUserName.return_value = [DomainModel.Bid(
    bided_user_name = "hoge",
    bid_item_id = 2,
    price = 1000,
    bided_at= datetime.datetime.now(),
)]


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(BidRepository, to=bid_repository_mock)
        binder.bind(ItemRepository, to=item_repository_mock)


class TestRegisterBid(unittest.TestCase):
    def test_ユーザーは同じ商品に一度しか入札できない(self):
        injector = Injector([DIModule()])
        bid_usecase = injector.get(BidUseCase)

        test_user_name = "hoge"
        test_item_id = 1
        test_price = 1000

        # 既に入札済みのユーザーの場合は例外を投げる
        with self.assertRaises(TypeError):
            bid_usecase.register_bid(test_user_name, test_item_id, test_price)
