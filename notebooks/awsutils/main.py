'''
(C) Crown Copyright, Met Office. All rights reserved.
This file is part of PyPrecis and is released under the BSD 3-Clause license.
See LICENSE in the root of the repository for full licensing details.
'''
from fetch_s3_file import copy_s3_files, find_matching_s3_keys
import iris
import os




def load_data(inpath):

    if inpath.startswith('s3'):
        keys = find_matching_s3_keys(inpath)
        s3dir = get_directory(inpath)
        temp_path = '/tmp'
        for key in keys:
            file = key.split('/')[-1]
            if os.path.exists(os.path.join(temp_path,file)) == 0:
                copy_s3_files(os.path.join(s3dir,key), temp_path)
            else:
                print(key, ' already exist')

        files = inpath.split('/')[-1]
        data = iris.load(os.path.join(temp_path,files))
        return data


def get_directory(inpath):
    path = inpath.split('/')
    dirpath='s3://'
    for p in path[2:-1]:
        dirpath = os.path.join(dirpath,p)
    return dirpath



def main():
    inpath = 's3://ias-pyprecis/data/sample_data.nc'
    data = load_data(inpath)
    print(data)


if __name__ == "__main__":
    main()