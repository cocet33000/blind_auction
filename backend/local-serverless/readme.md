# ローカルでAPIGateway+Lambda+DyanmoDBをテスト

# 起動方法
docker-composeで起動
```bash
docker-compose up
```
下記3個のDockerコンテナが起動する
- apigateway+lambda
- dynamodb
- dynamodb admin

lambda+apigatewayのエミュレートはserverless frameworkを使用。エンドポイントやlambdaのエントリーポイントの定義はserverless.ymlで行っている。

## テスト
コンテナを起動すると、localhost:3333でAPIのエンドポイントが起動。  
本番と同様のhttpリクエストで各APIを実行可能
```bash
curl -X 'GET' 'http://localhost:3333/bids' -H 'accept:application/json'
```


