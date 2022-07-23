from main.domain.shared.event import Event
from main.infrastructure.event_publisher_impl import EventPublisherImpl


# ローカルでは、コンテナで立てたDynamoDBでテスト
# CI/CDではテスト対象がないためとりあずコメントアウトしておく

# def test_イベントをストアに格納できる():
#     event = Event("test", {"test": "test"})
#     res = EventPublisherImpl.publish(event)

#     assert not res.get("is_error")
