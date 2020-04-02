#!/bin/bash -l
#SBATCH --qos=normal
#SBATCH --mem=100G
#SBATCH --ntasks=8
#SBATCH --time=00-06:00:00
module load scitools
python3 -u /project/precis/worksheets/data/pp/wks5dataprep.py
