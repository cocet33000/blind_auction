from UseCase import get_items
from UseCase import register_item
from UseCase import register_bid
from UseCase import get_bids_by_user

print(get_items())
print(register_bid(user_name="fuga", item_id=4, price=10000))
print(
    register_item(
        name="hoge",
        image_src="http://test",
        description="hoge hoge",
        start_price=100,
    )
)
print(get_bids_by_user(user_name="hoge"))
