from __future__ import annotations

from main.presentation.lambda_handler import api_handler

from mock import Mock

from main.usecase import ItemUseCase
from main.usecase import BidUseCase


item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)

event = {
    "pathParameters": {"proxy": "not_exists_endpoint"},
    "requestContext": {"http": {"method": "GET"}},
}


def test_正常系():
    # TODO: リクエスト内容を別ファイルで用意する
    bid_usecase_mock.get_bids_by_user.return_value = "ok"
    response: dict = api_handler(event, "", item_usecase_mock, bid_usecase_mock)

    assert response.get("statusCode") == 404