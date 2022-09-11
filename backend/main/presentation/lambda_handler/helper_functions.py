from main.domain.auction import Status


def parse_event(event: dict):
    event_name = event["Records"][0]["dynamodb"]["NewImage"]["name"]["S"]
    event_details = event["Records"][0]["dynamodb"]["NewImage"]["details"]["M"]
    return event_name, event_details


def parser_bid_event(event_details: dict):
    item_id = event_details["item_id"]["S"]
    user_name = event_details["user_name"]["S"]
    price = event_details["price"]["N"]

    return item_id, user_name, price


def bids_by_user_serialize(bids_by_user: list):
    return [
        {
            "item_id": bid["item_id"],
            "user_name": bid["user_name"],
            "price": bid["price"],
        }
        for bid in bids_by_user
    ]


def parser_auction_event(event_details: dict):
    auction_id = event_details["auction_id"]["S"]
    auction_name = event_details["name"]["S"]
    type = Status.get_status(event_details["type"]["S"])

    return auction_id, auction_name, type
