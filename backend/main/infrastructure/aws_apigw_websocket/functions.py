from __future__ import annotations
import logging
import json
import boto3
import os

from dotenv import load_dotenv

# load_dotenv()
# table = boto3.resource(
#     "dynamodb", region_name=os.environ.get("AWS_REGION", "ap-northeast-1")
# ).Table(os.environ.get("AWS_DYNAMO_DB_WSCONNECTION_TABLE_NAME"))
# apigw = boto3.client(
#     "apigatewaymanagementapi",
#     endpoint_url=os.environ.get("AWS_APIGW_WSENDOPOINT_URL"),
#     region_name=os.environ.get("AWS_REGION", "ap-northeast-1"),
# )


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
