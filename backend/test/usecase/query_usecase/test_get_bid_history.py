from __future__ import annotations

from mock import Mock
from injector import Injector, Module, singleton

from main.domain.query import QueryRepository
from main.domain.query import BidHistory

from main.usecase import QueryUseCase

USER_NAME = "hoge"
query_repository_mock = Mock(spec=QueryRepository)
query_repository_mock.get_bid_history.return_value = BidHistory(USER_NAME, {})


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(QueryRepository, to=query_repository_mock)


def test_正常系():
    injector = Injector([DIModule()])
    query_usecase = injector.get(QueryUseCase)

    bid_history = query_usecase.get_bid_history(USER_NAME)

    assert USER_NAME == bid_history.get_user_name()
