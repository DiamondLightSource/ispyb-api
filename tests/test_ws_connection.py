import os

import ispyb.factory

def test_ws_connection():
    conf_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../conf/ws_config.cfg'))
    try:
        with ispyb.open(conf_file) as conn:
            pass
    except NotImplementedError:
        assert True
    else:
        assert False
