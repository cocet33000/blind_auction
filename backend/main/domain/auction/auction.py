from datetime import datetime
from enum import Enum

from ..shared.caller import get_caller_function_name
from ..shared.errors import ProhibitedGenerationError


class Status(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"

    # TODO: 絶対もっと良いやり方があるのでリファクタリングする
    @staticmethod
    def get_status(value):
        if value == "OPEN":
            return Status.OPEN
        elif value == "CLOSED":
            return Status.CLOSED


class Auction:
    def __init__(
        self,
        id: str,
        name: str,
        status: Status,
        start_datetime: datetime,
        end_datetime: datetime,
    ):
        # createtという関数以外からの呼び出し時はエラー
        caller_function_name = get_caller_function_name()
        if caller_function_name != "create" and caller_function_name != "reconstruct":
            raise ProhibitedGenerationError(
                "Auctionの生成はcreate関数とreconstruct関数のみが許可されています"
            )

        self._id = id
        self._name = name
        self._status = status
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "status": self._status.value,
            "start_datetime": self._start_datetime,
            "end_datetime": self._end_datetime,
        }

    def name(self) -> str:
        return self._name

    def isOpen(self) -> bool:
        return self._status == Status.OPEN

    @staticmethod
    def reconstruct(
        id: str,
        name: str,
        status: Status,
        start_datetime: datetime,
        end_datetime: datetime,
    ) -> "Auction":
        return Auction(
            id=id,
            name=name,
            status=status,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        )
