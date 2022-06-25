import uuid
import pytest
import datetime

from main.domain.bid import Bid
from main.domain.value_object import Price
from main.domain.shared.errors import ProhibitedGenerationError


def test_bidモデルを作成():
    BID_ID = "bid" + str(uuid.uuid4())
    BIDED_USER_NAME = "hoge"
    BID_ITEM_ID = "1"
    PRICE = 100
    BIDED_AT = datetime.datetime.now()

    bid = Bid.reconstruct(
        id=BID_ID,
        bided_user_name=BIDED_USER_NAME,
        bid_item_id=BID_ITEM_ID,
        price=Price(PRICE),
        bided_at=BIDED_AT,
    )

    assert bid.bided_user_name == BIDED_USER_NAME
    assert bid.bid_item_id == BID_ITEM_ID
    assert bid.price == Price(PRICE)
    assert bid.bided_at == BIDED_AT


def test_priceに文字列はNG():
    BID_ID = "bid" + str(uuid.uuid4())
    BIDED_USER_NAME = "hoge"
    BID_ITEM_ID = "1"
    PRICE_STR = "HOGE"
    BIDED_AT = datetime.datetime.now()

    with pytest.raises(TypeError):
        Bid.reconstruct(
            id=BID_ID,
            bided_user_name=BIDED_USER_NAME,
            bid_item_id=BID_ITEM_ID,
            price=PRICE_STR,  # type: ignore
            bided_at=BIDED_AT,
        )


def test_priceにint型はNG():
    BID_ID = "bid" + str(uuid.uuid4())
    BIDED_USER_NAME = "hoge"
    BID_ITEM_ID = "1"
    PRICE_INT = int(1000)
    BIDED_AT = datetime.datetime.now()

    with pytest.raises(TypeError):
        Bid.reconstruct(
            id=BID_ID,
            bided_user_name=BIDED_USER_NAME,
            bid_item_id=BID_ITEM_ID,
            price=PRICE_INT,  # type: ignore
            bided_at=BIDED_AT,
        )


def test_外部からのコンストラクタ呼び出しはNG():
    BID_ID = "bid" + str(uuid.uuid4())
    BIDED_USER_NAME = "hoge"
    BID_ITEM_ID = "1"
    PRICE = 100
    BIDED_AT = datetime.datetime.now()

    with pytest.raises(ProhibitedGenerationError):
        Bid(
            id=BID_ID,
            bided_user_name=BIDED_USER_NAME,
            bid_item_id=BID_ITEM_ID,
            price=Price(PRICE),
            bided_at=BIDED_AT,
        )
