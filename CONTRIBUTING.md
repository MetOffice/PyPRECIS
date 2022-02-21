# Contributing Guidelines

You'd like to help? Great!  :tada:

[Clone your own local copy](https://help.github.com/en/articles/cloning-a-repository) of this repositry run the following in your terminal:

```shell
git clone git@github.com:MetOffice/PyPRECIS.git
```

Consider [creating a conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) from the PyPRECIS dependencies specified in the `environment.yml` file:
```shell
conda env create -f environment.yml
```
Remember to activate your new environment:
```shell
conda activate pyprecis-environment
```

:exclamation: *Note: As of v1.0 we are unable to provison the model data necessary for reproducing the full PyPRECIS learning environment via github due to it's large file size.  Contact the PRECIS team for more information.*

## Before you start...
Read through the current issues to see what you can help with.  If you have your own ideas for improvements, please start a new issue so we can track and discuss your improvement. You must create a new branch for any changes you make.

**Please take note of the following guidelines when contributing to the PyPRECIS repository.**

* Please do **not** make changes to `main` or `develop` branches.  The `main` branch is reserved for files and code that has been fully tested and reviewed.  Only the core PyPRECIS developers can push to the `main` and `develop` branches.

* The `develop` branch contains the latest holistic version of the `PyPRECIS` repository.  Please branch off `develop` to fix a particular issue or add a new feature.
* Please use the following tokens at the start of a new branch name to help sign-post and group branches:

Name | Description
---- | -----------
new | Branch adding new code/files that don't exist in the repo
fix | Branch modifying code/files that already exist in the repo.
junk | Throwaway branch created to experiment

* Git can pattern match branches to to give you an overview of all (e.g. fix) branches:
 ```shell
 git branch --list "fix/*"
 ```
* Use a forward slash to separate the token from the branch name. For example:
```
new/Wks10
fix/Wks2_units
```
* When you think your branch is ready to be merged into `develop`, open a new pull request.

## Signposting
* **Issues** are tracked and discussed under the Issues tab.  Please use issues to disucss proposed changes or capture improvements needed to work towards the next milestone.  Issues or improvements that contribute to the next milestone to be captured in thr Wiki tab.
* **Pull requests** show branches that are currently under review.  New pull requests are created in reponse to branch fixes identified and recorded in the Issues tab.
* **Wiki** is used for summarising update aims for future versions of the notebooks, and to record speculative improvements that cannot be action in the current milestone.



Other more general points to note:

* **Avoid long descriptive names.**  Long branch names can be very helpful when you are looking at a list of branches but it can get in the way when looking at decorated one-line logs as the branch names can eat up most of the single line and abbreviate the visible part of the log.
* **Do not use bare numbers.** Do not use use bare numbers (or hex numbers) as part of your branch naming scheme.

## CONTRIBUTING.ipynb
The `CONTRIBUTING.ipyn` file contains the worksheet style guide.  Please consult this for information on formatting the new and ammended worksheets in a consistent style.

**If in doubt, please contact the PRECIS team (precis@metoffice.gov.uk) if you
have questions.**

<h5 align="center">
<img src="notebooks/img/MO_MASTER_black_mono_for_light_backg_RBG.png" width="200" alt="Met Office"> <br>
&copy; British Crown Copyright 2018 - 2022, Met Office
</h5>
