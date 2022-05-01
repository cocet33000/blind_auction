from dataclasses import dataclass


@dataclass
class Item:
    """_summary_
    """
    name: str
    number: int
    description: str
    start_price: int
    bided_num: int

    def __hash__(self):
        return hash(self.name) & hash(self.number)
