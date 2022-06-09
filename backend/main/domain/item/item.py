from dataclasses import dataclass, asdict

from ..value_object.price import Price


@dataclass
class Item:
    id: str
    name: str
    image_src: str
    description: str
    start_price: Price
    bid_num: int

    def to_dict(self) -> dict:
        return asdict(self)
