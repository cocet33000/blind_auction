from main.infrastructure import QueryUsecaseImpl


def test_正常系():
    QueryUsecaseImpl.get_bid_history("test")
