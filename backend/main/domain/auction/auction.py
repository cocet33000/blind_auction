from datetime import datetime, timedelta
from enum import Enum
from datetime import timezone


from ..shared.caller import get_caller_function_name
from ..shared.errors import ProhibitedGenerationError
from ..shared import Event


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


class Period(object):
    def __init__(self, start_datetime: datetime, end_datetime: datetime):
        self.start_datetime = start_datetime.astimezone(timezone(timedelta(hours=9)))
        self.end_datetime = end_datetime.astimezone(timezone(timedelta(hours=9)))

    def __eq__(self, other):
        return (
            self.start_datetime == other.start_datetime
            and self.end_datetime == other.end_datetime
        )

    def to_dict(self):
        return {
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
        }


class AuctionEvent(Event):
    def __init__(self, auction_id, auction_name, type: Status) -> None:
        event_name = "AUCTION"
        event_details = {
            "auction_id": auction_id,
            "name": auction_name,
            "type": type,
        }
        super().__init__(event_name, event_details)

    def auction_id(self):
        return self.event_details.get("auction_id")

    def type(self):
        return self.event_details.get("type")

    def name(self):
        return self.event_details.get("name")


class Auction:
    def __init__(
        self,
        id: str,
        name: str,
        status: Status,
        period: Period,
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
        self._period = period

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "status": self._status.value,
            "start_datetime": self.start_datetime(),
            "end_datetime": self.end_datetime(),
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
            period=Period(start_datetime, end_datetime),
        )

    def switchStatus(self, now_datetime):
        now_datetime = now_datetime.astimezone(timezone(timedelta(hours=9)))

        pre_status = self._status
        if self.start_datetime() > now_datetime:
            self._status = Status.CLOSED
        if self.start_datetime() < now_datetime:
            self._status = Status.OPEN
        if self.end_datetime() < now_datetime:
            self._status = Status.CLOSED

        # statusを更新した場合のみ、イベントを返却
        return (
            AuctionEvent(
                auction_id=self._id,
                auction_name=self._name,
                type=self._status,
            )
            if self._status != pre_status
            else None
        )

    def start_datetime(self):
        return self._period.start_datetime

    def end_datetime(self):
        return self._period.end_datetime
