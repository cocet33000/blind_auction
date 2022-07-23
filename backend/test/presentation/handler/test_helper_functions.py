from main.presentation.lambda_handler import parse_event
from main.presentation.lambda_handler import parser_bid_event

event = {
    "Records": [
        {
            "eventID": "d0ae1bdc2b7af7865fe5ec5c3b354827",
            "eventName": "INSERT",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "ap-northeast-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1658563931,
                "Keys": {"id": {"S": "eec2b9ff-552a-4c54-aeef-dfd027411848"}},
                "NewImage": {
                    "name": {"S": "BID"},
                    "details": {
                        "M": {
                            "item_id": {"S": "a0da31b7-d106-4797-b21b-c616edbb7dce"},
                            "user_name": {"S": "cocet330000"},
                            "price": {"N": "555"},
                        }
                    },
                    "id": {"S": "eec2b9ff-552a-4c54-aeef-dfd027411848"},
                },
                "SequenceNumber": "227700000000011710313103",
                "SizeBytes": 167,
                "StreamViewType": "NEW_IMAGE",
            },
            "eventSourceARN": "arn:aws:dynamodb:ap-northeast-1:442019341120:table/blind_auction_events/stream/2022-07-23T07:52:01.413",
        }
    ]
}


def test_parse_event():
    event_name, event_details = parse_event(event)
    assert "BID" == event_name


def test_parse_bid_event():
    event_name, event_details = parse_event(event)
    item_id, user_name, price = parser_bid_event(event_details)

    assert "cocet330000" == user_name
    assert "a0da31b7-d106-4797-b21b-c616edbb7dce" == item_id
    assert "555" == price
