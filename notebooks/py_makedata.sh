#!/bin/bash -l
#SBATCH --qos=normal
#SBATCH --mem=100G
#SBATCH --ntasks=8
#SBATCH --time=00-06:00:00

# (C) Crown Copyright, Met Office. All rights reserved.
# This file is part of PyPrecis and is released under the BSD 3-Clause license.
# See LICENSE in the root of the repository for full licensing details.

module load scitools
python3 -u /project/ciid/projects/PRECIS/worksheets/data/pp/wks5dataprep.py
