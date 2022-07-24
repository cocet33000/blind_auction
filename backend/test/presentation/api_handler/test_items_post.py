from __future__ import annotations
import json

from main.presentation.lambda_handler import api_handler

from main.domain.shared import DomainException

from mock import Mock

from main.usecase import ItemUseCase
from main.usecase import BidUseCase

item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)

event = {
    "pathParameters": {"proxy": "items"},
    "requestContext": {"http": {"method": "POST"}},
    "body": """{"name": "hoge", "image_src": "test.png", "description": "hoge", "start_price": 100}""",
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    item_usecase_mock.register_item.return_value = "OK"
    response: dict = api_handler(event, "", item_usecase_mock, bid_usecase_mock)

    assert response.get("statusCode") == 200


def test_異常系():
    item_usecase_mock.register_item.side_effect = DomainException("NG")
    response: dict = api_handler(event, "", item_usecase_mock, bid_usecase_mock)
    body = json.loads(response.get("body"))

    assert response.get("statusCode") == 500
    assert body.get("message") == "NG"
