from injector import inject

from main.domain.query import QueryRepository
from main.domain.query import BidHistory


class QueryUseCase:
    @inject
    def __init__(self, query_repository_impl: QueryRepository):
        self.query_repository = query_repository_impl

    def get_bid_history(self, user_id: str) -> BidHistory:
        return self.query_repository.get_bid_history(user_id)
