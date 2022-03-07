
import io
import os
import boto3
from urllib.parse import urlparse
from fnmatch import fnmatch
from shutil import copyfile
import iris


def _fetch_s3_file(s3_uri, save_to):

    bucket_name, key = _split_s3_uri(s3_uri)
    # print(f"Fetching s3 object {key} from bucket {bucket_name}")

    client = boto3.client("s3")
    obj = client.get_object(
        Bucket=bucket_name,
        Key=key,
    )
    with io.FileIO(save_to, "w") as f:
        for i in obj["Body"]:
            f.write(i)


def _save_s3_file(s3_uri, out_filename, file_to_save="/tmp/tmp"):
    bucket, folder = _split_s3_uri(s3_uri)
    out_filepath = os.path.join(folder, out_filename)
    # print(f"Save s3 object {out_filepath} to bucket {bucket}")
    client = boto3.client("s3")
    client.upload_file(
        Filename=file_to_save,
        Bucket=bucket,
        Key=out_filepath
    )


def _split_s3_uri(s3_uri):
    parsed_uri = urlparse(s3_uri)
    return parsed_uri.netloc, parsed_uri.path[1:]


def find_matching_s3_keys(in_fileglob):

    bucket_name, file_and_folder_name = _split_s3_uri(in_fileglob)
    folder_name = os.path.split(file_and_folder_name)[0]
    all_key_responses = _get_all_files_in_s3_folder(bucket_name, folder_name)
    matching_keys = []
    for key in [k["Key"] for k in all_key_responses]:
        if fnmatch(key, file_and_folder_name):
            matching_keys.append(key)
    return matching_keys


def _get_all_files_in_s3_folder(bucket_name, folder_name):
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
    '''
    This function copy files from s3 bucket to local directory.
    args
    ---
    in_fileglob: s3 uri of flies (wild card can be used)
    out_folder: local path where data will be stored
    '''
    matching_keys = find_matching_s3_keys(in_fileglob)
    in_bucket_name = _split_s3_uri(in_fileglob)[0]
    out_scheme = urlparse(out_folder).scheme
    for key in matching_keys:
        new_filename = os.path.split(key)[1]
        temp_filename = os.path.join("/tmp", new_filename)
        in_s3_uri = os.path.join("s3://{}".format(in_bucket_name), key)
        _fetch_s3_file(in_s3_uri, temp_filename)
        if out_scheme == "s3":
            _save_s3_file(
                out_folder,
                new_filename,
                temp_filename,
            )
        else:
            copyfile(
                temp_filename, os.path.join(out_folder, new_filename)
            )
        os.remove(temp_filename)


def load_data(inpath):
    '''
    This methods copy the data from s3 bucket and load the data as iris cubelist. 
    Data is stored in data/ directory.

    input: file(s) path on s3 bucket
    output: iris cubelist
    '''
    if inpath.startswith('s3'):
        keys = find_matching_s3_keys(inpath)
        s3dir = _get_directory(inpath)
        temp_path = 'data/'
        if os.path.exists(temp_path) == 0:
            os.mkdir(temp_path)

        for key in keys:
            file = key.split('/')[-1]
            if os.path.exists(os.path.join(temp_path, file)) == 0:
                print(os.path.join(s3dir, file))
                copy_s3_files(os.path.join(s3dir, file), temp_path)
            else:
                print(key, ' already exist')
        files = inpath.split('/')[-1]
        data = iris.load(os.path.join(temp_path, files))

        return data


def _get_directory(inpath):
    path = inpath.split('/')
    dirpath = 's3://'
    for p in path[2:-1]:
        dirpath = os.path.join(dirpath, p)
    return dirpath


def flush_data(path):
    '''
    It delete the data from compute node. 

    Input: file(s) path
    '''
    import glob
    files = glob.glob(path)
    for file in files:
        os.remove(file)


def main():
    in_fileglob = 's3://ias-pyprecis/data/cmip5/.nc'
    out_folder = '/home/h01/zmaalick/myprojs/PyPRECIS/aws-scripts'
    copy_s3_files(in_fileglob, out_folder)


if __name__ == "__main__":
    main()
