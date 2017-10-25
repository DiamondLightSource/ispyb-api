from __future__ import absolute_import, division, print_function

import io
import os
import re

from setuptools import find_packages, setup

# cf.
# https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
def read(*names, **kwargs):
  with io.open(
    os.path.join(os.path.dirname(__file__), *names),
    encoding=kwargs.get("encoding", "utf8")
  ) as fp:
    return fp.read()

def find_version(*file_paths):
  version_file = read(*file_paths)
  version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                            version_file, re.M)
  if version_match:
    return version_match.group(1)
  raise RuntimeError("Unable to find version string.")

setup(
    name='ispyb',
    version=find_version("ispyb", "__init__.py"),
    description='ISPyB library based on stored procedures',
    url='https://github.com/DiamondLightSource/ispyb-api',
    author='Karl Erik Levik',
    author_email='scientificsoftware@diamond.ac.uk',
    keywords = ['ISPyB', 'database'],
    packages=find_packages(),
    install_requires=[
      'mysql-connector<2.2.3',
    ],
    setup_requires=[
      'pytest-runner',
    ],
    tests_require=[
      'mock',
      'pytest',
    ],
    classifiers = [
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Operating System :: OS Independent',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
