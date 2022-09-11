from enum import Enum

from ..value_object import Price
from ..shared.caller import get_caller_function_name
from ..shared.errors import ProhibitedGenerationError


class Status(Enum):
    BEFORE_AUCTION = "before_auction"
    UP_FOR_AUCTION = "up_for_auction"
    SOLD_OUT = "sold_out"

    # TODO: 絶対もっと良いやり方があるのでリファクタリングする
    @staticmethod
    def get_status(value):
        if value == "before_auction":
            return Status.BEFORE_AUCTION
        elif value == "up_for_auction":
            return Status.UP_FOR_AUCTION
        elif value == "sold_out":
            return Status.SOLD_OUT


class Item:
    def __init__(
        self,
        id: str,
        status: Status,
        name: str,
        image_src: str,
        description: str,
        start_price: Price,
        auction_id: str,
        bid_num: int,
    ):
        # createtという関数以外からの呼び出し時はエラー
        caller_function_name = get_caller_function_name()
        if caller_function_name != "create" and caller_function_name != "reconstruct":
            raise ProhibitedGenerationError("Itemの生成はcreate関数とreconstruct関数のみが許可されています")

        self.id = id
        self.name = name
        self.status = status
        self.image_src = image_src
        self.description = description
        self.auction_id = auction_id

        if not isinstance(start_price, Price):
            raise TypeError
        self.start_price = start_price

        self.bid_num = bid_num

    def to_up_for_auction(self):
        self.status = Status.UP_FOR_AUCTION

    def to_sold_out(self):
        self.status = Status.SOLD_OUT

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "status": self.status.value,
            "name": self.name,
            "image_src": self.image_src,
            "description": self.description,
            "start_price": int(self.start_price),
            "bid_num": self.bid_num,
            "auction_id": self.auction_id,
        }

    @staticmethod
    def reconstruct(
        id: str,
        status: Status,
        name: str,
        image_src: str,
        description: str,
        start_price: Price,
        bid_num: int,
        auction_id: str,
    ) -> "Item":
        return Item(
            id=id,
            status=status,
            name=name,
            image_src=image_src,
            description=description,
            start_price=start_price,
            bid_num=bid_num,
            auction_id=auction_id,
        )
