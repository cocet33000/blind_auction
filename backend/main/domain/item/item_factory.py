import uuid
from injector import inject

from main.domain.shared import DomainException

from .item import Item
from .item import Status
from ..value_object.price import Price

from ..auction import AuctionRepository


class ItemFactory:
    @inject
    def __init__(self, auction_reository: AuctionRepository):
        self.auction_repository = auction_reository

    def create(self, name, image_src, description, start_price, auction_id) -> Item:
        def getNewId() -> str:
            return str(uuid.uuid4())

        try:
            self.auction_repository.getById(auction_id)
        except Exception as e:
            raise DomainException(e)

        new_id = getNewId()

        domain_start_price = Price(start_price)

        return Item(
            id=new_id,
            status=Status.BEFORE_AUCTION,
            name=name,
            image_src=image_src,
            description=description,
            start_price=domain_start_price,
            bid_num=0,
            auction_id=auction_id,
        )
