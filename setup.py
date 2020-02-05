from __future__ import absolute_import, division, print_function

from setuptools import find_packages, setup
import sys

INSTALL_REQUIRES = ["mysql-connector-python", "tabulate"]

if sys.version_info.major == 2:
    INSTALL_REQUIRES.append("enum34")

setup(
    name="ispyb",
    version="5.6.0",
    description="Python package to access ISPyB database",
    long_description="This package provides a python interface to ISPyB. It can access the ISPyB database directly or (in future versions) run on top of the official ISPyB webservices API.",
    url="https://github.com/DiamondLightSource/ispyb-api",
    author="Karl Erik Levik, Markus Gerstel",
    author_email="scientificsoftware@diamond.ac.uk",
    download_url="https://github.com/DiamondLightSource/ispyb-api/releases",
    keywords=["ISPyB", "database"],
    packages=find_packages(),
    scripts=["bin/dimple2ispyb.py", "bin/mxdatareduction2ispyb.py"],
    license="Apache License, Version 2.0",
    install_requires=INSTALL_REQUIRES,
    setup_requires=["pytest-runner"],
    tests_require=["mock", "pytest"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={"libtbx.precommit": ["ispyb = ispyb"]},
    project_urls={"Documentation": "https://ispyb.readthedocs.io"},
)
