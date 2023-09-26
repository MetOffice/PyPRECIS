"""
(C) Crown Copyright, Met Office. All rights reserved.
This file is part of PyPrecis and is released under the BSD 3-Clause license.
See LICENSE in the root of the repository for full licensing details.
"""
import os
from tqdm import tqdm
import boto3


def upload_folder_to_s3(s3_client, s3bucket, input_dir, s3_path):
    # This method uploads the directory (also subdirectories) to S3.
    # You can also specify the s3 bucket directory where to store data
    pbar = tqdm(os.walk(input_dir))
    for path, subdirs, files in pbar:
        for file in files:
            dest_path = path.replace(input_dir, "").replace(os.sep, "/")
            s3_file = f"{s3_path}/{dest_path}/{file}".replace("//", "/")
            local_file = os.path.join(path, file)
            s3_client.upload_file(local_file, s3bucket, s3_file)
            pbar.set_description(f"Uploaded {local_file} to {s3_file}")
    print(f"Successfully uploaded {input_dir} to S3 {s3_path}")


def main():
    s3_client = boto3.client("s3")
    upload_folder_to_s3(
        s3_client, "ias-pyprecis", "/data/users/fris/s3_uploads/pp", "data/pp"
    )


if __name__ == "__main__":
    main()
