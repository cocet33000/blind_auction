from __future__ import annotations

from mock import Mock
from injector import Injector, Module, singleton

from main.usecase import QueryUseCase

USER_NAME = "hoge"

query_usecase_mock = Mock(spec=QueryUseCase)
query_usecase_mock.get_bid_history.return_value = {}


@singleton
class DIModule(Module):
    def configure(self, binder):
        binder.bind(QueryUseCase, to=query_usecase_mock)


def test_正常系():
    injector = Injector([DIModule()])
    query_usecase = injector.get(QueryUseCase)

    bid_history = query_usecase.get_bid_history(USER_NAME)

    assert {} == bid_history
