
import io
import os
import boto3
from urllib.parse import urlparse
from fnmatch import fnmatch
from shutil import copyfile


def fetch_s3_file(s3_uri, save_to):

    bucket_name, key = split_s3_uri(s3_uri)
    print(f"Fetching s3 object {key} from bucket {bucket_name}")

    client = boto3.client("s3")
    obj = client.get_object(
        Bucket=bucket_name,
        Key=key,
    )
    with io.FileIO(save_to, "w") as f:
        for i in obj["Body"]:
            f.write(i)


def save_s3_file(s3_uri, out_filename, file_to_save="/tmp/tmp"):
    bucket, folder = split_s3_uri(s3_uri)
    out_filepath = os.path.join(folder, out_filename)
    print(f"Save s3 object {out_filepath} to bucket {bucket}")
    client = boto3.client("s3")
    client.upload_file(
        Filename=file_to_save,
        Bucket=bucket,
        Key=out_filepath
    )


def split_s3_uri(s3_uri):
    parsed_uri = urlparse(s3_uri)
    return parsed_uri.netloc, parsed_uri.path[1:]


def find_matching_s3_keys(in_fileglob):

    bucket_name, file_and_folder_name = split_s3_uri(in_fileglob)
    folder_name = os.path.split(file_and_folder_name)[0]
    all_key_responses = get_all_files_in_s3_folder(bucket_name, folder_name)
    matching_keys = []
    for key in [k["Key"] for k in all_key_responses]:
        if fnmatch(key, file_and_folder_name):
            matching_keys.append(key)
    return matching_keys


def get_all_files_in_s3_folder(bucket_name, folder_name):
    client = boto3.client("s3")
    response = client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=folder_name,
    )
    all_key_responses = []
    if "Contents" in response:
        all_key_responses = response["Contents"]
    while response["IsTruncated"]:
        continuation_token = response["NextContinuationToken"]
        response = client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=folder_name,
            ContinuationToken=continuation_token,
        )
        if "Contents" in response:
            all_key_responses += response["Contents"]
    return all_key_responses


def copy_s3_files(in_fileglob, out_folder):
    matching_keys = find_matching_s3_keys(in_fileglob)
    in_bucket_name = split_s3_uri(in_fileglob)[0]
    out_scheme = urlparse(out_folder).scheme
    for key in matching_keys:
        new_filename = os.path.split(key)[1]
        temp_filename = os.path.join("/tmp", new_filename)
        in_s3_uri = os.path.join(f"s3://{in_bucket_name}", key)
        print(in_bucket_name)
        print(key)
        print(in_s3_uri)
        fetch_s3_file(in_s3_uri, temp_filename)
        if out_scheme == "s3":
            save_s3_file(
                out_folder,
                new_filename,
                temp_filename,
            )
        else:
            copyfile(
                temp_filename, os.path.join(out_folder, new_filename)
            )
        os.remove(temp_filename)


def main():
    in_fileglob = 's3://ias-pyprecis/data/cordex/afr-44/tas_AFR-44_MOHC-HadGEM2-ES_rcp85_r1i1p1_KNMI-RACMO22T_v2_day_*.nc'
    out_folder = '/net/home/h01/zmaalick/myprojs/PyPRECIS/aws-scripts'
    copy_s3_files(in_fileglob, out_folder)


if __name__ == "__main__":
    main()
