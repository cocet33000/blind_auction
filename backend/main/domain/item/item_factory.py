from .item import Item
import uuid


class ItemFactory:
    @staticmethod
    def Create(name, image_src, description, start_price) -> Item:
        def getNewId() -> str:
            return str(uuid.uuid4())

        new_id = getNewId()

        return Item(
            id=new_id,
            name=name,
            image_src=image_src,
            description=description,
            start_price=start_price,
            bid_num=0,
        )
