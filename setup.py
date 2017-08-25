from __future__ import absolute_import, division
from setuptools import setup, find_packages
import io
import os
import re
import sys

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

setup(name='ispyb',
      description='Python API for ISPyB',
      url='https://github.com/DiamondLightSource/python-ispyb',
      author='Markus Gerstel',
      author_email='markus.gerstel@diamond.ac.uk',
      download_url="https://github.com/DiamondLightSource/python-ispyb/releases",
      version=find_version("ispyb", "__init__.py"),
      install_requires=['enum-compat',
                        'mysql-connector<2.2.3'],
      packages=find_packages(),
      license='BSD',
      setup_requires=['pytest-runner'],
      tests_require=['mock',
                     'pytest'],
      classifiers = [
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
     )
