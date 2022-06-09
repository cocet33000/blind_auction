from .item import Item

# ドメインがインフラに依存しているのでここは書き直す
from ...infrastructure.dynamo_db.sequence import Sequence


class ItemFactory:
    @staticmethod
    def Create(name, image_src, description, start_price) -> Item:
        def getNewId():
            sequence = Sequence("items")
            sequence.update(actions=[Sequence.current_number.add(1)])
            return sequence.current_number

        new_id = getNewId()

        return Item(
            id=new_id,
            name=name,
            image_src=image_src,
            description=description,
            start_price=start_price,
            bid_num=0,
        )
