import ispyb
import ispyb.model


class Container(ispyb.model.DBCache):
    """An object representing a Container database entry. The object
    lazily accesses the underlying database when necessary and exposes record
    data as python attributes.
    """

    def __init__(self, containerid, db_conn, preload=None):
        """Create a Container object for a defined ContainerID. Requires
        a database connection object exposing further data access methods.

        :param containerid: ContainerID
        :param db_conn: ISPyB database connection object
        :return: A Container object representing the database entry for
                 the specified ContainerID
        """
        self._db = db_conn
        self._containerid = int(containerid)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError("Loading containers is not currently supported")

    @property
    def containerid(self):
        """Returns the ID associated with this container information."""
        return self._containerid

    def __bool__(self):
        """Container object evaluates to True in a boolean context if container
        information exists in the database. Otherwise it evaluates to False."""
        self.load()
        return self._data is not None

    __nonzero__ = __bool__  # Python 2 compatibility

    def __repr__(self):
        """Returns an object representation, including the ContainerID,
        the database connection interface object, and the cache status."""
        return "<Container #%d (%s), %r>" % (
            self._containerid,
            "cached" if self.cached else "uncached",
            self._db,
        )

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "Container #%d (not yet loaded from database)" % self._containerid
        return ("\n".join(("Container #{0.containerid}",))).format(self)


ispyb.model.add_properties(
    Container,
    (
        ("owner_given_name", "ownerGivenName", "Given name of the container owner"),
        ("owner_family_name", "ownerFamilyName", "Family name of the container owner"),
        (
            "priority_processing",
            "processingPipelineName",
            "Selected priority processing pipeline",
        ),
    ),
)
