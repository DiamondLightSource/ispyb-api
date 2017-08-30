from __future__ import absolute_import, division

import pytest

# Functions from
# https://docs.pytest.org/en/latest/example/simple.html
# to support marker for incremental tests.

def pytest_runtest_makereport(item, call):
  if "incremental" in item.keywords:
    if call.excinfo is not None:
      parent = item.parent
      parent._previousfailed = item

def pytest_runtest_setup(item):
  if "incremental" in item.keywords:
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
      pytest.xfail("previous test failed (%s)" %previousfailed.name)
