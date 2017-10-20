import ispyb.factory
import os

def test_ws_connection():
    conf_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../conf/ws_config.cfg'))
    try:
        conn = ispyb.factory.create_connection(conf_file)
    except NotImplementedError:
        assert True
    else:
        assert False
