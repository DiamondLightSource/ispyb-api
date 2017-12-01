from __future__ import absolute_import, division, print_function

import ispyb
import pytest

def test_ws_connection(testconfig_ws):
  with pytest.raises(NotImplementedError):
     with ispyb.open(testconfig_ws) as conn:
        pass
