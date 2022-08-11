from __future__ import annotations
import logging
import json
import boto3
import os

from dotenv import load_dotenv

# 一旦、パラメータをハードコーディング
load_dotenv()
table = boto3.resource(
    "dynamodb", region_name="ap-northeast-1"
).Table("blind-auction-websocket-connections")
apigw = boto3.client(
    "apigatewaymanagementapi",
    endpoint_url=os.environ.get("https://wss.blind-auction.com/deb"),
    region_name=os.environ.get("ap-northeast-1"),
)


def send_comment_Bid_num_increase(item_id: str, bid_num: float) -> bool:
    try:
        print(f"{item_id} {bid_num} ")
        connections = table.scan().get("Items", [])
        for connection in connections:
            if connection.get("id"):
                print(connection.get("id"))
                apigw.post_to_connection(
                    Data=json.dumps({"item_id": item_id, "bid_num": bid_num}),
                    ConnectionId=connection.get("id"),
                )
    except Exception as e:
        logging.error(e)
        return False
    return True
