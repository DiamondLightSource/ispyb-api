import pytest

import ispyb


def test_ws_connection(testconfig_ws):
    with pytest.raises(NotImplementedError):
        with ispyb.open(testconfig_ws) as conn:
            assert conn
