from main.domain.item import ItemFactory


def test_itemを生成():
    item = ItemFactory.create("hoge", "hoge", "hoge", 100)
    assert item.id is not None
    assert item.name == "hoge"
    assert item.image_src == "hoge"
    assert item.description == "hoge"
    assert item.start_price == 100
    assert item.bid_num == 0
