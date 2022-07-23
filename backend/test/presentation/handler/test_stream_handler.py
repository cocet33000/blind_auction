from __future__ import annotations
from main.domain import bid

from main.presentation.lambda_handler import stream_handler

from mock import Mock

from main.domain.item.bid_event_subscriber import BidEventSubscriber
from main.usecase import ItemUseCase
from main.usecase import BidUseCase


item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)
bid_event_subscriber_mock = Mock(spec=BidEventSubscriber)


def test_正常系():
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
                                "item_id": {
                                    "S": "a0da31b7-d106-4797-b21b-c616edbb7dce"
                                },
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
    context = {}
    assert 200 == stream_handler(
        event, context, item_usecase_mock, bid_usecase_mock, bid_event_subscriber_mock
    ).get("statusCode")


def test_異常系_パースエラー():
    event = {}
    context = {}
    assert 500 == stream_handler(
        event, context, item_usecase_mock, bid_usecase_mock, bid_event_subscriber_mock
    ).get("statusCode")
