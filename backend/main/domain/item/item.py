from ..value_object import Price
from ..shared.caller import get_caller_function_name
from ..shared.errors import ProhibitedGenerationError


class Item:
    def __init__(
        self,
        id: str,
        name: str,
        image_src: str,
        description: str,
        start_price: Price,
        bid_num: int,
    ):
        # createtという関数以外からの呼び出し時はエラー
        caller_function_name = get_caller_function_name()
        if caller_function_name != "create" and caller_function_name != "reconstruct":
            raise ProhibitedGenerationError("Itemの生成はcreate関数とreconstruct関数のみが許可されています")

        self.id = id
        self.name = name
        self.image_src = image_src
        self.description = description

        if not isinstance(start_price, Price):
            raise TypeError
        self.start_price = start_price

        self.bid_num = bid_num

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "image_src": self.image_src,
            "description": self.description,
            "start_price": int(self.start_price),
            "bid_num": self.bid_num,
        }

    @staticmethod
    def reconstruct(
        id: str,
        name: str,
        image_src: str,
        description: str,
        start_price: Price,
        bid_num: int,
    ) -> "Item":
        return Item(id, name, image_src, description, start_price, bid_num)
