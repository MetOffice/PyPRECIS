# Contributing Guidelines

You'd like to help? Great!  :tada:

To clone your own local copy of this repositry run the following in your terminal:

```
git clone git@github.com:MetOffice/PyPRECIS.git
```

**Please take note of the following guidelines when contributing to the PyPRECIS repository.**

* Please do **not** make changes to the `master` branch.  The `master` branch is reserved for files and code that has been fully tested and reviewed.  If you think something is ready to be pushed to the `master` branch please check with Saeed or Hamish first.

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

## Signposting
* **Issues** are tracked and discussed under the Issues tab.  Please use issues to disucss proposed changes or capture improvements needed to work towards the next milestone.  Issues or improvements that contribute to the next milestone to be captured in thr Wiki tab.
* **Pull requests** show branches that are currently under review.  New pull requests are created in reponse to branch fixes identified and recorded in the Issues tab.
* **Wiki** is used for summarising update aims for future versions of the notebooks, and to record speculative improvements that cannot be action in the current milestone.



Other more general points to note:

* **Avoid long descriptive names.**  Long branch names can be very helpful when you are looking at a list of branches but it can get in the way when looking at decorated one-line logs as the branch names can eat up most of the single line and abbreviate the visible part of the log.
* **Do not use bare numbers.** Do not use use bare numbers (or hex numbers) as part of your branch naming scheme.

**If in doubt, please contact the PRECIS team (precis@metoffice.gov.uk) if you
have questions**

<h5 align="center">
<img src="notebooks/img/MO_MASTER_black_mono_for_light_backg_RBG.png" style="max-width: 40%;" alt="Met Office"> <br>
&copy; British Crown Copyright 2018 - 2019, Met Office
</h5>
