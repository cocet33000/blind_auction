import os

from dotenv import load_dotenv
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pynamodb.attributes import NumberAttribute
from pynamodb.attributes import MapAttribute
from pynamodb.indexes import LocalSecondaryIndex, GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import UTCDateTimeAttribute

from main.domain.bid import Bid as DomainModelBid
from main.domain.item import Item as DomainModelItem
from main.domain.item import Status as DomainModelItemStatus
from main.domain.auction import (
    Auction as DomainModelAuction,
    Status as DomainModelAuctionStatus,
)
from main.domain.value_object import Price


class BidsByUserNameIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = "bidsByUsername-GSI"
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    bided_user_name = UnicodeAttribute(hash_key=True)
    id = UnicodeAttribute(range_key=True)


class Bid(Model):
    class Meta:
        load_dotenv()
        if os.environ.get("MODE") == "local":
            host = "http://localhost:8000"
        table_name = os.environ.get("AWS_DYNAMO_DB_ITEMS_TABLE_NAME")
        region = os.environ.get("AWS_REGION")

    id = UnicodeAttribute(hash_key=True)
    range_key = UnicodeAttribute(range_key=True)
    price = NumberAttribute(null=False)
    bided_user_name = UnicodeAttribute(null=False)
    bided_at = UTCDateTimeAttribute(null=False)
    bidsByUserNameIndex = BidsByUserNameIndex()

    def to_model(self) -> DomainModelBid:
        return DomainModelBid.reconstruct(
            id=self.range_key,
            bided_user_name=self.bided_user_name,
            bided_at=self.bided_at,
            bid_item_id=self.id,
            price=Price(self.price),
        )


class GetAllItemsIndex(LocalSecondaryIndex):
    class Meta:
        index_name = "name-index"
        projection = AllProjection()

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(range_key=True)


class Item(Model):
    class Meta:
        load_dotenv()
        if os.environ.get("MODE") == "local":
            host = "http://localhost:8000"
        table_name = os.environ.get("AWS_DYNAMO_DB_ITEMS_TABLE_NAME")
        region = os.environ.get("AWS_REGION")

    id = UnicodeAttribute(hash_key=True)
    # statusを追加する
    range_key = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute(null=False)
    image_src = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=False)
    start_price = NumberAttribute(null=False)
    bid_num = NumberAttribute(null=False)
    getAllItemsIndex = GetAllItemsIndex()

    def to_model(self) -> DomainModelItem:
        return DomainModelItem.reconstruct(
            id=self.id,
            status=DomainModelItemStatus.BEFORE_AUCTION,
            name=self.name,
            image_src=self.image_src,
            description=self.description,
            start_price=Price(self.start_price),
            bid_num=int(self.bid_num),
        )


class Event(Model):
    class Meta:
        load_dotenv()
        if os.environ.get("MODE") == "local":
            host = "http://localhost:8000"
        table_name = os.environ.get("AWS_DYNAMO_DB_EVENTS_TABLE_NAME")
        region = os.environ.get("AWS_REGION")

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    details = MapAttribute(null=False)


class Auction(Model):
    class Meta:
        load_dotenv()
        if os.environ.get("MODE") == "local":
            host = "http://localhost:8000"
        table_name = os.environ.get("AWS_DYNAMO_DB_ITEMS_TABLE_NAME")
        region = os.environ.get("AWS_REGION")

    id = UnicodeAttribute(hash_key=True)
    range_key = UnicodeAttribute(range_key=True)
    auction_name = UnicodeAttribute(null=False)
    auction_status = UnicodeAttribute(null=False)
    auction_start_datetime = UTCDateTimeAttribute(null=False)
    auction_end_datetime = UTCDateTimeAttribute(null=False)

    def to_model(self) -> DomainModelAuction:
        return DomainModelAuction.reconstruct(
            id=self.range_key,
            name=self.auction_name,
            status=DomainModelAuctionStatus.get_status(self.auction_status),  # type: ignore
            start_datetime=self.auction_start_datetime,
            end_datetime=self.auction_end_datetime,
        )
