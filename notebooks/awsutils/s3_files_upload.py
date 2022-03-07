# this script load data on aws s3 bucket
import botocore
import boto3
import logging
import os
import glob


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
        s3_client.upload_file(file_name, bucket, object_name)
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    bucket = "ias-pyprecis"

    file_path = "*.txt"
    files = glob.glob(file_path)

    for file in files:
        upload_file(file, bucket, object_name=None)


if __name__ == "__main__":
    main()
