# PyPRECIS

<h4 align="center">
PyPRECIS is the python based training environment for Met Office PRECIS training courses.
</h4>

<p align="center">
<!-- Github Sheilds - comment out until repo is public -->
<!-- https://shields.io/ is a good source of these -->
<a href="https://github.com/MetOffice/PyPRECIS/releases">
    <img src="https://img.shields.io/github/tag/MetOffice/PyPRECIS.svg"
        alt="Latest version" /></a>
<a href="https://github.com/MetOffice/PyPRECIS/commits/master">
     <img src="https://img.shields.io/github/commits-since/MetOffice/PyPRECIS/latest.svg"
          alt="Commits since last release" /></a>
<img src="https://img.shields.io/github/release-date/MetOffice/PyPRECIS.svg"
    alt="Release date" /></a>
<img src="https://img.shields.io/github/repo-size/MetOffice/PyPRECIS.svg"
    alt="Repo size" /></a>
<img alt="GitHub" src="https://img.shields.io/github/license/metoffice/PyPRECIS?style=flat">
    </p>
<br>



## Overview
PyPRECIS forms part of the Met Office PRECIS regional climate modelling system.  It is principally designed as a learning tool to faciliate processing of regional climate model (RCM) output.  It is desgined to be used in conjunction with taught workshops in an instructor led environment.

PyPRECIS is built on [Jupyter Notebooks](https://jupyter.org/), with data processing performed in python, making use of [Iris](https://scitools.org.uk/iris/docs/latest/).

Further information about PRECIS can be found on the [Met Office website](https://www.metoffice.gov.uk/precis).

## Contents
The teaching elements of PyPRECIS are contained in the `notebooks` directory. The core primary worksheets are:

Worksheet | Aims
:----: | -----------
[1](notebooks/worksheet1.ipynb) | <li>Identify and list the names of PRECIS output data in PP format using standard Linux commands</li><li>Use basic Iris commands to load data files, and view Iris cubes</li><li>Use Iris commands to remove the model rim, select data variables and save the output as NetCDF files</li>
[2](notebooks/worksheet2.ipynb) | <li>Apply basic statistical operations to Iris cubes</li><li>Plot information from Iris cubes</li>
[3](notebooks/worksheet3.ipynb) | <li>Extract specific regions of interested from large datasets</li><li>Apply more advanced statistical operations to multi-annual data</li><li>Produce your own data processing workflow</li>  
[4](notebooks/worksheet4.ipynb) | <li>Calculate difference and percentage differences across cubes</li><li>Plot cubes using different plotting methods and with an appropriate colour scale</li><li>Create time series anomalies of precipitation and tempeature</li>  
[5](notebooks/worksheet5.ipynb) | <li>Have an appreciation for working with daily model data</li><li>Understand how to calculate some useful climate extremes statistics</li><li>Be aware of some coding stratagies for dealing with large data sets</li></ul>  
[6](notebooks/worksheet6.ipynb) | An extended coding exercise designed to allow you to put everything you've learned into practise  

Additional tutorials specific to the CSSP 20th Century reanalysis dataset:

Worksheet | Aims
:----: | -----------
[CSSP 1](notebooks/CSSP_20CRDS_Tutorials/Introduction.ipynb) | <li>How to use a cloud based platform to analyse the 20CR-DS dataset</li><li>Settig up a python environment</li>
[CSSP 2](notebooks/CSSP_20CRDS_Tutorials/tutorial_1_data_access.ipynb) | <li>How to load data into Xarrays format</li><li>How to convert the data xarrays into iris cube format</li><li>How to perform basic cube operations</li>
[CSSP 3](notebooks/CSSP_20CRDS_Tutorials/tutorial_3_basic_analysis.ipynb) | <li>Calculate and visualise annual and monthly means</li><li>Calculate and visualise seasonal means</li><li>Calculate mean differences (anomalies)</li>
[CSSP 4](notebooks/CSSP_20CRDS_Tutorials/tutorial_4_advance_analysis.ipynb) | <li>Calculate frequency of wet days</li><li>Calculate percentiles</li><li>Calculate some useful climate extremes statistics</li>

Three additional worksheets are available for use by workshop instructors:

* `makedata.ipynb`: Provides scripts for preparing raw model output for use in notebook exercises.
* `worksheet_solutions.ipyn`: Solutions to worksheet exercices.
* `worksheet6example.ipynb`: Example code for Worksheet 6.

## Data
Data relating to the PyPRECIS project is currently held internally to the Met Office.

The total data volume for the core worksheets is 36.68 GB, of which ~20 GB is raw pp data. This is too large to be stored on github, or via git lfs.
As of v2.0, the storage solution for making this data available alongside the notebooks is still under investgation.

Data relating to the **CSSP 20CRDS** tutorials is held online in an Azure Blob Storage Service. To access this data user will need a valid shared access signature (SAS) token.  The data is in [Zarr](https://zarr.readthedocs.io/en/stable/) format and the total volume is ~2TB. The data is in hourly, 3 hourly, 6 hourly, daily and monthly frequencies stored seperatrely under the `metoffice-20cr-ds` container on MS-Azure. Monthly data only is also via [Zenodo](https://zenodo.org/record/2558135).


# create s3 bucket

* goto s3 service and press "create bucket"
* name the bucket
* set region to EU (London) eu-west-2
* add tags:
  * Name: [name of bucket or any unique name]
  * ServiceOwner: [your-name]
  * ServiceCode: PABCLT
  * Tenable: FA
* click on "create bucket"

## Key configurations


The above script run only when config files contains latest keys. In order to update the keys:

* go to AB climate training dev --> Administrator access --> command line or programmatic access
* Copy keys in "Option 1: Set AWS environment variables"
* In VDI, paste (/replace existing) these keys in ~/.aws/config
* add [default] in first line
* Copy keys in "Option 2: Add a profile to your AWS credentials file"
* In VDI, Paste the keys in credentials file: ~/.aws/credentials (remove the first copied line, looks somethings like: [198477955030_AdministratorAccess])
* add [default] in first line

The config and credentials file should look like (with own keys): 

'''
[default]
export AWS_ACCESS_KEY_ID="ASIAS4NRVH7LD2RRGSFB"
export AWS_SECRET_ACCESS_KEY="rpI/dxzQWhCul8ZHd18n1VW1FWjc0LxoKeGO50oM"
export AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEGkaCWV1LXdlc3QtMiJH"
'''

## Loading data on s3 bucket from VDI (using boto3)

to upload the file(s) on S3 use: /aws-scripts/s3_file_upload.py
to upload the directory(s) on S3 use: /aws-scripts/s3_bulk_data_upload.py


## Contributing
Information on how to contribute can be found in the [Contributing guide](CONTRIBUTING.md).
Please also consult the `CONTRIBUTING.ipynb` for information on formatting the worksheets in Jupyter Notebooks.  **Note** that we do not currently make use of Jupyter Lab as it doesn't currently support the types of html formatting we use in Jupyter Notebooks.

## Licence
PyPRECIS is licenced under BSD 3-clause licence for use outside of the Met Office.

<h5 align="center">
<img src="notebooks/img/MO_MASTER_black_mono_for_light_backg_RBG.png" width="200" alt="Met Office"> <br>
&copy; British Crown Copyright 2018 - 2022, Met Office
</h5>
