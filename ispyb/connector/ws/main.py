import ispyb.interface.connection


class ISPyBWSConnector(ispyb.interface.connection.IF):
    """Provides a connector to an ISPyB database through webservices."""

    def __init__(self, user=None, pw=None, url="http://localhost"):
        raise NotImplementedError("Connection type ispyb_ws not implemented")

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass

    def disconnect(self):
        pass

    def get_data_area_package(self):
        return "ispyb.ws"
