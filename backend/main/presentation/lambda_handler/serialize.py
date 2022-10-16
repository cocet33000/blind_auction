from main.presentation.openapi_server.models.open_auction import OpenAuction
from main.presentation.openapi_server.models.items import Items
from main.presentation.openapi_server.models.item import Item

from ..openapi_server.models.bid_historys import BidHistorys
from ..openapi_server.models.bid_history import BidHistory
from ..openapi_server.models.bid_history_bid import BidHistoryBid
from ..openapi_server.models.bid_history_item import BidHistoryItem
from ..openapi_server.models.auction import Auction
from ..openapi_server.models.auctions_get_response import AuctionsGetResponse
from ..openapi_server.models.home_get_response import HomeGetResponse

from ..openapi_server.models.commands_auctions_response import CommandsAuctionsResponse
from ..openapi_server.models.auction_event import AuctionEvent


def bids_history_serialize(bid_historys: list):
    return BidHistorys(
        bid_historys=[
            BidHistory(
                item=BidHistoryItem(
                    id=bid_history["item"]["id"],
                    name=bid_history["item"]["name"],
                    image_src=bid_history["item"]["image_src"],
                    description=bid_history["item"]["description"],
                    start_price=bid_history["item"]["start_price"],
                ),
                bid=BidHistoryBid(
                    price=bid_history["bid"]["price"],
                    bided_at=bid_history["bid"]["bided_at"].isoformat(),
                ),
            )
            for bid_history in bid_historys
        ]
    ).to_dict()


def auctions_get_reonse_seririalize(auctions) -> dict:
    auctions_dict = [auction.to_dict() for auction in auctions]

    return AuctionsGetResponse(
        auctions=[
            Auction(
                id=auction_dict["id"],
                name=auction_dict["name"],
                status=auction_dict["status"],
                start_date=auction_dict["start_datetime"].isoformat(),
                end_date=auction_dict["end_datetime"].isoformat(),
            )
            for auction_dict in auctions_dict
        ],
        has_next=False,
    ).to_dict()


def home_get_response_serialize(_auction, _items) -> dict:
    auction = OpenAuction(
        id=_auction.id(),
        name=_auction.name(),
        start_date=_auction.start_datetime().isoformat(),
        end_date=_auction.end_datetime().isoformat(),
    )

    items = Items(
        has_next=False,
        items=[Item.from_dict(_item.to_dict()) for _item in _items],
    )
    return HomeGetResponse(auction=auction, items=items).to_dict()


def commands_auctions_response_serialize(auction_events) -> dict:
    events = [
        AuctionEvent(
            id=auction_event.auction_id(),
            name=auction_event.name(),
            status=auction_event.type().value,
        )
        for auction_event in auction_events
    ]

    return CommandsAuctionsResponse(events=events).to_dict()
