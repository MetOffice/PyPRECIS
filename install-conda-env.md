# How to Install the PyPRECIS Conda Environment

## What is Conda?
Conda is a piece of software that allows for the convenient management of open source libraries (i.e. Numpy) and environments, most usually utilised for the Python programming language. This powerful tool allows users to create and manage multiple environments upon the same system, finding and installing the packages required to populate them, whilst ensuring ensuring there are no conflicts. Environments can be readily maintained with a few simple commands and shared between systems, with varying degrees of exactness. More information can be found in the [official Conda documentation](https://docs.conda.io/en/latest/).

Conda should already be installed and configured on the systems being utilised. Met Office users will need to follow the instructions located [here](https://www-avd/sci/software_stack/conda_initial_how_to.html) to finalise the configuration of their conda.

You can check that conda is installed upon your system using
`conda --version`, this should return the version number of your current conda install. If you require general help around the usage of conda this can be obtained using `conda --help`.

## Installing the PyPRECIS Environment
In order to open the [jupyter notebooks](https://jupyter.org/) in this repository and run the code contained within, the installation of provided conda environment is required. This can be installed using either the `environment.yml` or `pyprecis-environment.lock.yml` files (both in the top directory of this repo), it is recommended that the lock file is utilised for this process. The difference between the two files is the lock defines exactly the versions of the packages that should be utilised to create the environment, where as the standard yml files just specifies the packages and lets conda solve for an environment without conflicts.

If you need to check whether the environment has already been installed, then this can be done by viewing a list of all installed environments using `conda env list`.

The PyPRECIS environment can be installed using `conda env create -n pyprecis -f pyprecis-environment.lock.yml`. Once this command has finished executing then the environment can be activated using `conda activate pyprecis`. You can tell that you have activated the environment as its name will be pre-pended to the terminal command line. When you have finished using the environment you can exit it using `conda deactivate`.

A list of the packages installed into a conda environment can be viewed using `conda list` (*notice the omission of `env`*). This will return a complete list of all package names, version number, build name and the channel they were obtained from.
