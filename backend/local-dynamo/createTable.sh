cd `dirname $0`
aws dynamodb create-table --cli-input-json file://config/amtest-blind-auction-items.json --endpoint-url http://localhost:8000 --region ap-northeast-1
aws dynamodb create-table --cli-input-json file://config/blind_auction_events.json --endpoint-url http://localhost:8000 --region ap-northeast-1