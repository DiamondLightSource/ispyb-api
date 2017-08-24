from __future__ import absolute_import, division
from setuptools import setup, find_packages
import sys

# to release increment this number:
package_version = '0.4'
# and run the following on a bash prompt:
'''
export NUMBER="$(grep package_version setup.py | head -1 | cut -d"'" -f 2)";
git add -u; git commit -m "v${NUMBER} release"; git tag -a v${NUMBER} -m v${NUMBER}; git push; git push origin v${NUMBER}
python setup.py sdist upload
'''

if sys.version_info < (2,7):
  sys.exit('Sorry, Python < 2.7 is not supported')

setup(name='ispyb',
      description='Python API for ISPyB',
      url='https://github.com/DiamondLightSource/python-ispyb',
      author='Markus Gerstel',
      author_email='markus.gerstel@diamond.ac.uk',
      download_url="https://github.com/DiamondLightSource/python-ispyb/releases",
      version=package_version,
      install_requires=['enum-compat',
                        'mysql-connector<2.2.3'],
      packages=find_packages(),
      license='BSD',
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
