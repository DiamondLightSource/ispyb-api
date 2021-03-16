import ispyb
from ispyb.connector.mysqlsp.main import ISPyBMySQLSPConnector


def test_session_from_envvar(testconfig, monkeypatch):
    monkeypatch.setenv("ISPYB_CREDENTIALS", testconfig)
    conn = ispyb.open()
    assert isinstance(conn, ISPyBMySQLSPConnector)
