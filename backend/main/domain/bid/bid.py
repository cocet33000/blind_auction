from datetime import datetime

from ..value_object.price import Price
from ..shared import get_caller_function_name
from ..shared.errors import ProhibitedGenerationError


class Bid:
    def __init__(
        self,
        id: str,
        bided_user_name: str,
        bid_item_id: str,
        price: Price,
        bided_at: datetime,
    ):
        # createtという関数以外からの呼び出し時はエラー
        caller_function_name = get_caller_function_name()
        if caller_function_name != "create" and caller_function_name != "reconstruct":
            raise ProhibitedGenerationError("Bidの生成はcreate関数とreconstruct関数のみが許可されています")

        self.id = id
        self.bided_user_name = bided_user_name
        self.bid_item_id = bid_item_id

        if not isinstance(price, Price):
            raise TypeError
        self.price = price

        self.bided_at = bided_at

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "bided_user_name": self.bided_user_name,
            "bid_item_id": self.bid_item_id,
            "price": self.price,
            "bided_at": self.bided_at.strftime("%Y/%m/%d %H:%M"),
        }

    @staticmethod
    def reconstruct(
        id: str,
        bided_user_name: str,
        bid_item_id: str,
        price: Price,
        bided_at: datetime,
    ) -> "Bid":
        return Bid(id, bided_user_name, bid_item_id, price, bided_at)
