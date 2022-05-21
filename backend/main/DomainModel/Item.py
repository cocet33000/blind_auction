from dataclasses import dataclass, asdict


@dataclass
class Item:
    id: int
    name: str
    image_src: str
    description: str
    start_price: int
    bid_num: int

    def __post_init__(self):
        if not (isinstance(self.id, int) and isinstance(self.name, str) and isinstance(self.image_src, str) and isinstance(self.description, str) and isinstance(self.start_price, int) and isinstance(self.bid_num, int)):
            raise TypeError
        if not (1 <= self.id < 100000000):
            raise ValueError
        if not (0 <= self.start_price < 1000000):
            raise ValueError
        if not (0 <= self.bid_num < 100000000):
            raise ValueError

    def to_dict(self) -> dict:
        return asdict(self)
