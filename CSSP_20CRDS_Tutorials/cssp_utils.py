import iris
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

import numpy as np
import os
import xarray as xr




def zarr_reader(path, freq):

    ZARR = os.path.join(path,freq)
    ds = xr.open_zarr(ZARR)
    for xvars in ds:
        ds[xvars].attrs['iris_coord_system'] = '{"grid_north_pole_latitude": 51.81999969482422, "grid_north_pole_longitude": 289.8299865722656,                         "ellipsoid": {"semi_major_axis": 6371229.0}, "coord_system_name": "rotated_latitude_longitude"}'

    return ds
