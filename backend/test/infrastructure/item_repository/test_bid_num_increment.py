from main.infrastructure.item_repository_impl import ItemRepositoryImpl

# ローカルでは、コンテナで立てたDynamoDBでテスト
# CI/CDではテスト対象がないためとりあずコメントアウトしておく
# def test_正常系():
#     item_id = "f99dd977-7635-456b-bdb9-1b4da09f9696"
#     ItemRepositoryImpl.bidNumIncrement(item_id)
