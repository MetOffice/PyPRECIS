# Contributing Guidelines

You'd like to help? Great!  :tada:

All contributions to `PyPRECIS` are made via merges with the main branch.
New contributors should add their details to the "code contributors" section of this document as part of their first request.
The developer who reviews each pull request is responsible for checking that the contributor's name is listed in this file before merging the changes into main branch.

## Code Contributors  

 *  Hamish Steptoe (Met Office, UK), @hsteptoe
 *  Zubair Maalick (Met Office, UK when contributing) @zmaalick
 *  Nicholas Savage (Met Office, UK), @nhsavage
 *  Saeed Sadri (Met Office, UK when contributing) @balazagi
 *  Grace Redmond (Met Office, UK), @gredmond-mo
 *  Rosanna Amato (Met Office, UK), @rosannaamato
 *  Joshua Wiggs (Met Office, UK), @JoshuaWiggs


## Contributor Licence Agreement and Certificate of Origin  
By making a contribution to this project, I certify that:  
* The contribution was created in whole or in part by me and I have the right to submit it, either on my behalf or on behalf of
my employer, under the terms and conditions as described by this file; or  
* The contribution is based upon previous work that, to the best of my knowledge, is covered under an appropriate licence and
I have the right or permission from the copyright owner under that licence to submit that work with modifications, whether
created in whole or in part by me, under the terms and conditions as described by this file; or  
* The contribution was provided directly to me by some other person who certified it or I have not modified it.  
* I understand and agree that this project and the contribution are public and that a record of the contribution
(including my name and email address) is retained for the full term of the copyright and may be redistributed
consistent with this project or the licence(s) involved.  
* I, or my employer, grant to the UK Met Office and all recipients of this software a perpetual, worldwide, non-exclusive,
no-charge, royalty-free, irrevocable copyright licence to reproduce, modify, prepare derivative works of, publicly display,
publicly perform, sub-licence, and distribute this contribution and such modifications and derivative works consistent with
this project or the licence(s) involved or other appropriate open source licence(s) specified by the project and approved by
the [Open Source Initiative (OSI)](https://opensource.org/)  
* If I become aware of anything that would make any of the above inaccurate, in any way, I will let the UK Met Office know as
soon as I become aware.  

(The `PyPRECIS` Contributor Licence Agreement and Certificate of Origin is inspired by the Certificate of Origin
used by Enyo and the Linux Kernel.)

## Developing changes

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

* Please do **not** make changes directly to the `main` branch.  The `main` branch is reserved for files and code that has been fully tested and reviewed.  Only the core PyPRECIS developers can push to the the `main` branch.

* The `main` branch contains the latest holistic version of the `PyPRECIS` repository.  Please branch off `main` to fix a particular issue or add a new feature.
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
* When you think your branch is ready to be merged into `main`, open a new pull request.

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
&copy; British Crown Copyright 2018 - 2023, Met Office
</h5>
