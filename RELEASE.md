## How to prepare a release

First, ensure that you have updated `HISTORY.rst` with the changes for the new release and committed the changes.

To prepare an ISPyB API release you need to install the package [bump2version](https://pypi.org/project/bump2version/):

```bash
pip install bump2version
```

and then, in the repository directory, run one of the following

```bash
# assuming current version is 1.2.3
bumpversion patch  # release version 1.2.4
bumpversion minor  # release version 1.3.0
bumpversion major  # release version 2.0.0
```

This automatically creates a release commit and a release tag.
You then need to push both to the Github repository:
```bash
git push  # pushes the release commit
git push origin v2.0.0  # pushes the release tag for version 2.0.0
```

Assuming the tests pass the release is then created by Travis and uploaded directly onto [pypi](https://pypi.org/project/ispyb/).

The ISPyB API is also released on [conda-forge](https://github.com/conda-forge/ispyb-feedstock), the release process there will be triggered automatically within a few hours.
