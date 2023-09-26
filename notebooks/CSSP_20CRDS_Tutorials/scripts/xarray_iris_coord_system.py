"""
(C) Crown Copyright, Met Office. All rights reserved.
This file is part of PyPrecis and is released under the BSD 3-Clause license.
See LICENSE in the root of the repository for full licensing details.
"""
import json

import iris
import iris.coord_systems
import xarray as xr


class XarrayIrisCoordSystem(object):
    coord_systems_lookup = {
        "latitude_longitude": iris.coord_systems.GeogCS,
        "rotated_latitude_longitude": iris.coord_systems.RotatedGeogCS,
        "mercator": iris.coord_systems.Mercator,
    }

    def __init__(self):
        self._cube = None
        self._data_array = None

        self.coord_system_attr_name = "iris_coord_system"

    @property
    def cube(self):
        return self._cube

    @cube.setter
    def cube(self, value):
        self._cube = value

    @property
    def data_array(self):
        return self._data_array

    @data_array.setter
    def data_array(self, value):
        self._data_array = value

    def _attrs_as_dict(self, attrs):
        return {k: v for (k, v) in attrs}

    def _store_coord_system(self):
        coord_system = self.cube.coord_system()
        attrs = self._attrs_as_dict(coord_system._pretty_attrs())
        # We don't want the default ellipsoid attr, which is a reference to an Iris class.
        attrs["ellipsoid"] = self._attrs_as_dict(coord_system.ellipsoid._pretty_attrs())
        attrs["coord_system_name"] = coord_system.grid_mapping_name
        return json.dumps(attrs)

    def _build_ellipsoid(self, ellipsoid_kwargs):
        return iris.coord_systems.GeogCS(**ellipsoid_kwargs)

    def _build_coord_system(self, coord_system_str):
        coord_system_dict = json.loads(coord_system_str)
        coord_system_name = coord_system_dict.pop("coord_system_name")
        ellipsoid_kwargs = coord_system_dict.pop("ellipsoid")

        ellipsoid = self._build_ellipsoid(ellipsoid_kwargs)

        constructor = self.coord_systems_lookup.get(coord_system_name)
        if constructor is not None:
            result = constructor(**coord_system_dict, ellipsoid=ellipsoid)
        else:
            raise ValueError(
                f"Coord system name {coord_system_name!r} is either not known or supported."
            )
        return result

    def from_iris(self, cube):
        self.cube = cube

        data_array = xr.DataArray.from_iris(self.cube)
        data_array.attrs[self.coord_system_attr_name] = self._store_coord_system()

        self.data_array = data_array
        return self.data_array

    def to_iris(self, data_array):
        self.data_array = data_array
        coord_system_str = self.data_array.attrs.pop(self.coord_system_attr_name, None)

        self.cube = self.data_array.to_iris()
        if coord_system_str is not None:
            cube_coord_system = self._build_coord_system(coord_system_str)
            for axis in ["X", "Y"]:
                try:
                    self.cube.coord(axis=axis).coord_system = cube_coord_system
                except AttributeError:
                    pass

        return self.cube
