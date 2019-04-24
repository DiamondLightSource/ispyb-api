import abc

ABC = abc.ABCMeta(
    "ABC", (object,), {"__slots__": ()}
)  # compatible with Python 2 *and* 3


class DataArea(ABC):
    def set_connection(self, conn):
        self.conn = conn

    def get_connection(self):
        if hasattr(self, "conn"):
            return self.conn
