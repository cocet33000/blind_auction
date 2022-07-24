from datetime import datetime
from enum import Enum


class Status(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class Auction:
    def __init__(
        self,
        name: str,
        status: Status,
        start_datetime: datetime,
        end_datetime: datetime,
    ):
        self._name = name
        self._status = status
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
