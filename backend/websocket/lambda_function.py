import json
import os
import logging
import boto3

dynamodb = boto3.resource('dynamodb')
apigw = boto3.client('apigatewaymanagementapi',
                     endpoint_url=os.environ.get("ENDPOINT_URL"))
table = dynamodb.Table(os.environ.get("TABLE_NAME"))


logger = logging.getLogger()

if log_level := os.environ.get("LOG_LEVEL"):
    logger.setLevel(log_level)


def lambda_handler(event, context):
    route_key = event.get("requestContext", {}).get("routeKey", "")
    logger.debug(json.dumps(event))
    if route_key:
        if route_key == "$connect":
            connection_id = event.get(
                "requestContext", {}).get("connectionId", "")
            responce = on_connect(connection_id)
            return responce
        elif route_key == "$disconnect":
            connection_id = event.get(
                "requestContext", {}).get("connectionId", "")
            responce = on_disconnect(connection_id)
            return responce
        elif route_key == "bid":
            input_item_id = json.loads(event.body).get("item_id")
            input_bid_num = json.loads(event.body).get("bid_num")
            if input_bid_num and input_bid_num:
                responce = bid_event_publish(
                    item_id=input_item_id, bid_num=input_bid_num)
                return responce
            else:
                return {
                    'statusCode': 500,
                    'body': json.dumps('bad request')
                }

    else:
        return {
            'statusCode': 500,
            'body': json.dumps('error!')
        }


def bid_event_publish(item_id, bid_num):
    try:
        connections = table.scan().get("Items", [])
    except:
        return {
            'statusCode': 500,
            'body': json.dumps('error!')
        }
    for connection in connections:
        if connection.get("id"):
            apigw.post_to_connection(
                Data=json.dumps({
                    "item_id": item_id,
                    "bid_num": bid_num
                }),
                ConnectionId=connection.get("id")
            )
    return{
        'statusCode': 200,
        'body': json.dumps('message send')
    }


def on_connect(connection_id):
    try:
        table.put_item(Item={"id": connection_id})
    except:
        return {
            'statusCode': 500,
            'body': json.dumps('error at connection')
        }
    return{
        'statusCode': 200,
        'body': json.dumps('Connected')
    }


def on_disconnect(connection_id):
    try:
        table.delete_item(Key={"id": connection_id})
    except:
        return {
            'statusCode': 500,
            'body': json.dumps('error at disconnection')
        }
    return{
        'statusCode': 200,
        'body': json.dumps('DiscSonnected')
    }
