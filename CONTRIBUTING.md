# Contributing Guidelines

Please take note of the following guidelines when contributing to the PyPRECIS repository:

* Please do **not** make changes to the `master` branch.  The `master` branch is reserved for files and code that has been fully tested and reviewed.  If you think something is ready to be pushed to the `master` branch please check with Saeed or Hamish first.
* The `develop` branch contains the latest holistic version of the `PyPRECIS` repository.  Please branch off `develop` to fix a particular issue or add a new feature.
* Please use the following tokens at the start of a new branch name to help sign-post and group branches:
```
new   Branch adding new code/files that don't exist in the repo.
fix   Branch modifying code/files that already exist in the repo.
junk  Throwaway branch created to experiment
```
 Git can pattern match branches to to give you an overview of all (e.g. fix) branches:
 ```
 git branch --list "fix/*"
 ```
* Use a forward slash to separate the token from the branch name. For example:
```
new/Worksheet5
fix/worksheet2aUnits
```

Other more general points to note:

* **Avoid long descriptive names.**  Long branch names can be very helpful when you are looking at a list of branches. But it can get in the way when looking at decorated one-line logs as the branch names can eat up most of the single line and abbreviate the visible part of the log.
* **Do not use bare numbers.** Do not use use bare numbers (or hex numbers) as part of your branch naming scheme.

**If in doubt, please contact Saeed Sadri (saeed.sadri@metoffice.gov.uk) or Hamish Steptoe (hamish.steptoe@metoffice.gov.uk) if you
have questions**
