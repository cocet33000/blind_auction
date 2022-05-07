from UseCase import get_items
from UseCase import register_item
from UseCase import register_bid

print(get_items())
print(register_bid(user_name="hoge", item_id=9, price=10000))
print(
    register_item(
        name="hoge",
        image_src="http://test",
        description="hoge hoge",
        start_price=100,
    )
)
