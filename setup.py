from setuptools import setup, find_packages

setup(
    name='ispyb-api',
    version='1.0.3',
    description='ISPyB library',
    url='https://github.com/DiamondLightSource/ispyb-api',
    author='Karl Erik Levik',
    keywords = ['ISPyB', 'database'], 
    packages=find_packages(),
    install_requires=['mysql-connector']
)
