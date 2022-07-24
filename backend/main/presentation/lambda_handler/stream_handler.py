from main.domain.bid import BidEvent
from main.usecase import ItemUseCase
from main.usecase import BidUseCase
from main.domain.item import BidEventSubscriber

from .helper_functions import parse_event, parser_bid_event


def stream_handler(
    event: dict,
    context,
    item_usecase: ItemUseCase,
    bid_usecase: BidUseCase,
    bid_event_subscriber: BidEventSubscriber,
):

    try:
        event_name, event_details = parse_event(event)
    except Exception as e:
        return {"statusCode": 500, "body": "NG"}

    try:
        if event_name == "BID":
            item_id, user_name, price = parser_bid_event(event_details)
            bid_event = BidEvent(item_id=item_id, user_name=user_name, price=price)
            bid_event_subscriber.consume(bid_event)
        return {"statusCode": 200, "body": "OK", "eventName": event_name}
    except Exception as e:
        return {"statusCode": 200, "body": "OK", "eventName": event_name}
