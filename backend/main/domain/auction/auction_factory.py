import uuid

from .auction import Auction
from .auction import Status


class AuctionFactory:
    @staticmethod
    def create(name: str, start_datetime, end_datetime) -> Auction:
        def getNewId() -> str:
            return "bid" + str(uuid.uuid4())

        new_id = getNewId()
        return Auction(
            id=new_id,
            name=name,
            status=Status.CLOSED,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        )
