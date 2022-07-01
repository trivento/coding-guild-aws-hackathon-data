import logging
import boto3
from botocore.exceptions import ClientError
import os
import sys


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def upload(bucket, filename, region):
    s3 = boto3.client('s3', region_name=region)
    with open(filename, "rb") as f:
        s3.upload_fileobj(f, bucket, filename)


if __name__ == '__main__':
    bucket = sys.argv[1]
    filename = sys.argv[2]
    region = len(sys.argv) > 3 and sys.argv[3] or 'eu-central-1'
    upload(bucket, filename, region)
