from dataclasses import dataclass, asdict


@dataclass
class Item:
    id: int
    name: str
    image_src: str
    description: str
    start_price: int
    bid_num: int

    def to_dict(self) -> dict:
        return asdict(self)
