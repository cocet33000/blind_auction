import uuid

from .item import Item
from ..value_object.price import Price


class ItemFactory:
    @staticmethod
    def create(name, image_src, description, start_price) -> Item:
        def getNewId() -> str:
            return str(uuid.uuid4())

        new_id = getNewId()

        domain_start_price = Price(start_price)

        return Item(
            id=new_id,
            name=name,
            image_src=image_src,
            description=description,
            start_price=domain_start_price,
            bid_num=0,
        )
