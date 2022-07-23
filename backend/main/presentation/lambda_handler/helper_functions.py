def parse_event(event: dict):
    event_name = event["Records"][0]["dynamodb"]["NewImage"]["name"]["S"]
    event_details = event["Records"][0]["dynamodb"]["NewImage"]["details"]["M"]
    return event_name, event_details


def parser_bid_event(event_details: dict):
    item_id = event_details["item_id"]["S"]
    user_name = event_details["user_name"]["S"]
    price = event_details["price"]["N"]

    return item_id, user_name, price
