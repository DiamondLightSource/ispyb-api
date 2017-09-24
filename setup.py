from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('ispyb/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name='ispyb',
    version=main_ns['__version__'],
    description='ISPyB library based on stored procedures',
    url='https://github.com/DiamondLightSource/ispyb-api',
    author='Karl Erik Levik',
    keywords = ['ISPyB', 'database'],
    packages=find_packages(),
    install_requires=['mysql-connector']
)
