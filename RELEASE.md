## How to prepare a release

To prepare an ISPyB API release you need to install the package bump2version

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
You then need to push those to the Github repository
```bash
git push; git push --tags
```

The release is then created by Travis and uploaded directly onto pypi.
