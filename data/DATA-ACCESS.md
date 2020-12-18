# Data Access

Data relating to the PyPRECIS project is currently stored at /project/ciid/projects/PRECIS/worksheets/data

The total data volume is 36.68 GB, of which ~20 GB is raw pp data. This is too large to be stored on github, or via git lfs.  
As of v1.0, the storage solution for making this data available alongside the notebooks is still under investgation.


Data relating to the CSSP_20CRDS_Tutorials is held online in an Azure Blob Storage Service. To access this data user will need a valid SAS (shared access signature) token.

The data is in Zarr format and the total volume is ~2TB. The data is in hourly, 3 hourly, 6 hourly, daily and monthly frequencies stored seperatrely uner the metoffice-20cr-ds container on MS-Azure.
A copy of this data is also available at Met office linux file system.