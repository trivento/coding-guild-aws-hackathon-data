import json
import boto3
import datetime
import matplotlib.pyplot as plt

REGION= 'eu-central-1'
AVAILABILITY_ZONE_A = f'{REGION}a'
AVAILABILITY_ZONE_B = f'{REGION}b'
AVAILABILITY_ZONE_C = f'{REGION}c'
INSTANCE_TYPE = 'm3.medium'

def create_client():
    client=boto3.client('ec2', region_name=REGION)
    return client

def get_spot_prices(availability_zone: str) -> dict:
    client = create_client()
    prices=client.describe_spot_price_history(
        InstanceTypes=[INSTANCE_TYPE],
        MaxResults=1000,
        ProductDescriptions=['Linux/UNIX (Amazon VPC)'],
        AvailabilityZone=availability_zone,
    )
    spot_prices=prices['SpotPriceHistory']
    for price in spot_prices:
        ts = price['Timestamp']
        price['Timestamp'] = int(ts.timestamp())
        price['timestamp_formatted'] = ts.strftime("%Y-%m-%d'T'%H:%M:%S%Z")
        price['date_short'] = ts.strftime("%d")
    return spot_prices

def plot_graph(az_a: dict, az_b: dict, az_c: dict) -> None:
    if az_a:
        x = []
        y = []
        for price in az_a:
            # x.append(price['Timestamp'])
            x.append(price['date_short'])
            y.append(float(price['SpotPrice']))

        x.reverse()
        y.reverse()
        plt.plot(x, y, label = AVAILABILITY_ZONE_A)

    if az_b:
        x = []
        y = []
        for price in az_b:
            # x.append(price['Timestamp'])
            x.append(price['date_short'])
            y.append(float(price['SpotPrice']))
        x.reverse()
        y.reverse()
        plt.plot(x, y, label = AVAILABILITY_ZONE_B)

    if az_c:
        x = []
        y = []
        for price in az_c:
            # x.append(price['Timestamp'])
            x.append(price['date_short'])
            y.append(float(price['SpotPrice']))
        x.reverse()
        y.reverse()
        plt.plot(x, y, label = AVAILABILITY_ZONE_C)

    # naming the x axis
    plt.xlabel('date')
    # naming the y axis
    plt.ylabel('price')

    plt.legend()

    # giving a title to my graph
    plt.title(f'spot prices for {INSTANCE_TYPE}')

    # function to show the plot
    plt.show()

if __name__ == '__main__':
    plot_graph(
        get_spot_prices(AVAILABILITY_ZONE_A),
        get_spot_prices(AVAILABILITY_ZONE_B),
        get_spot_prices(AVAILABILITY_ZONE_C),
    )
    # print(json.dumps(get_spot_prices(AVAILABILITY_ZONE_A)))