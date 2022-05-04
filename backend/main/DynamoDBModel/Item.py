import os

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
        if os.environ.get("MODE") == "local":
            host = "http://localhost:8000"
        table_name = os.environ.get("AWS_DYNAMO_DB_ITEMS_TABLE_NAME")
        region = os.environ.get("AWS_REGION")

    id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    image_src = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=False)
    start_price = NumberAttribute(null=False)
    bids = ListAttribute(of=Bid, null=True)

    def to_model(self):
        try:
            return myItem(
                name=self.name,
                image_src=self.image_src,
                description=self.description,
                start_price=self.start_price,
                bid_num=len(self.bids) if isinstance(self.bids, list) else 0,
            )
        except:
            return self
