import json
import boto3
import datetime

REGION = 'eu-central-1'
INSTANCE_TYPES = ['m3.medium']


def create_client():
    client = boto3.client('ec2', region_name=REGION)
    return client


def get_spot_prices(event):
    client = create_client()
    prices = client.describe_spot_price_history(
        InstanceTypes=INSTANCE_TYPES,
        MaxResults=1,
        # ProductDescriptions=['Linux/UNIX (Amazon VPC)'],
        # AvailabilityZone=availability_zone,
    )
    spot_prices = prices['SpotPriceHistory']
    print(prices)
    for price in spot_prices:
        ts = price['Timestamp']
        price['Timestamp'] = int(ts.timestamp())
        price['timestamp_formatted'] = ts.strftime("%Y-%m-%d'T'%H:%M:%S%Z")
        price['date_short'] = ts.strftime("%d")
    return spot_prices


def lambda_handler(event, context):
    # print(event)
    get_spot_prices(event)

    return {
        'statusCode': 200,
        'body':  {
            'result': 'ok'
        }
    }


if __name__ == '__main__':
    lambda_handler({
        'availabilityZones': ['eu-central-1a'],
        'instanceTypes': ['m3.medium'],
        'productDescriptions': ['Linux/UNIX (Amazon VPC)'],
        'maxResult': 10
    }, {})
