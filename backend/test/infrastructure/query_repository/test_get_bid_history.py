import uuid

from main.infrastructure.query_repository_impl import QueryReositoryImpl


def test_正常系():
    QueryReositoryImpl.get_bid_history("test")
