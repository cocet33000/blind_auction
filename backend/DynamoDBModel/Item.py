from dotenv import load_dotenv
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.attributes import NumberAttribute
from pynamodb.attributes import ListAttribute
from pynamodb.attributes import MapAttribute
from pynamodb.attributes import UTCDateTimeAttribute

from Model.Item import Item as myItem

class Bid(MapAttribute):
    price = NumberAttribute(null=False)
    bided_user_id = NumberAttribute(null=False)
    bided_at = UTCDateTimeAttribute(null=False)


class Item(Model):
    class Meta:
        load_dotenv()
        host = "http://localhost:8000"
        table_name = "blind_auction_items"
        region = 'ap-northeast-1'

    id = UnicodeAttribute(hash_key=True)
    number = NumberAttribute(null=False)
    name = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=False)
    start_price = NumberAttribute(null=False)
    bids = ListAttribute(of=Bid, null=True)

    def convert_to(self):
        return myItem(
            number=self.number,
            name=self.name,
            description=self.description,
            start_price=self.start_price,
            bided_num=len(self.bids) if isinstance(self.bids, list) else 0
        )
