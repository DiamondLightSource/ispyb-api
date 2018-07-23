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
    description='Python package to access ISPyB database',
    long_description='This package provides a python interface to ISPyB. It can access the ISPyB database directly or (in future versions) run on top of the official ISPyB webservices API.',
    url='https://github.com/DiamondLightSource/ispyb-api',
    author='Karl Erik Levik, Markus Gerstel',
    author_email='scientificsoftware@diamond.ac.uk',
    download_url='https://github.com/DiamondLightSource/ispyb-api/releases',
    keywords = ['ISPyB', 'database'],
    packages=find_packages(),
    scripts=['bin/dimple2ispyb.py', 'bin/mxdatareduction2ispyb.py'],
    license='Apache License, Version 2.0',
    install_requires=[
      'enum-compat',
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
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Operating System :: OS Independent',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
      'Documentation': 'https://ispyb.readthedocs.io',
    },
)
