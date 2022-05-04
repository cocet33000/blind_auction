from dataclasses import dataclass, asdict


@dataclass
class Item:
    name: str
    image_src: str
    description: str
    start_price: int
    bided_num: int

    def to_dict(self):
        return asdict(self)
