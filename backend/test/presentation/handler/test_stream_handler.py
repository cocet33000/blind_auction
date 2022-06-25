from __future__ import annotations

from main.presentation.lambda_handler import stream_handler

from mock import Mock

from main.usecase import ItemUseCase
from main.usecase import BidUseCase


item_usecase_mock = Mock(spec=ItemUseCase)
bid_usecase_mock = Mock(spec=BidUseCase)


def test_正常系():
    event = {}
    context = {}
    assert 200 == stream_handler(
        event, context, item_usecase_mock, bid_usecase_mock
    ).get("statusCode")
