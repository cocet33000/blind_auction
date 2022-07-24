from __future__ import annotations

from main.presentation.lambda_handler import api_handler

from main.domain.shared import DomainException

from mock import Mock

from main.usecase import ItemUseCase
from main.usecase import BidUseCase

item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)

event = {
    "pathParameters": {"proxy": "bids"},
    "requestContext": {"http": {"method": "GET"}},
    "queryStringParameters": {"user_name": "test"},
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    bid_usecase_mock.get_bids_by_user.return_value = "ok"
    response: dict = api_handler(event, "", item_usecase_mock, bid_usecase_mock)

    assert response.get("statusCode") == 200


def test_異常系():
    bid_usecase_mock.get_bids_by_user.side_effect = DomainException("error")
    response: dict = api_handler(event, "", item_usecase_mock, bid_usecase_mock)

    assert response.get("statusCode") == 500
