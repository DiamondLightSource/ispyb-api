import ispyb.model


class Sample(ispyb.model.DBCache):
    def __init__(self, sample_id, db_conn, preload=None):
        """Create a Sample object for a defined sample_id. Requires
        a database connection object exposing further data access methods.

        :param sample_id: bLSampleId
        :param db_conn: ISPyB database connection object
        :return: A Sample object representing the database entry for
                 the specified bLSampleId
        """
        self._db = db_conn
        self._id = int(sample_id)
        self._cache_container = None
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def id(self):
        "Returns the sampleId"
        return self._id

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "Sample #%d (not yet loaded from database)" % self._id
        return (
            "\n".join(
                (
                    "Sample #%s" % self._id,
                    "  Name         : %s" % self.name,
                    "  Crystal id   : %s"
                    % (self.crystal_id if self.crystal_id else "None"),
                    "  Container id : %s"
                    % (self.container_id if self.container_id else "None"),
                    "  DCIDs        : %s"
                    % (",".join(str(i) for i in self.dcids) if self.dcids else "None"),
                )
            )
        ).format(self)

    @property
    def container(self):
        """Returns the container information for the sample"""
        if self._cache_container is None:
            self.load()
            if not self._data["blSampleId"]:
                # Can not have a container without a sample
                self._cache_container = False
                return self._cache_container
            container = self._db.shipping.retrieve_container_for_sample_id(
                self._data["blSampleId"]
            )
            if not container:
                self._cache_container = False
            else:
                self._cache_container = ispyb.model.container.Container(
                    container[0]["containerId"], self._db, preload=container[0]
                )
        return self._cache_container


ispyb.model.add_properties(
    Sample,
    (
        ("name", "name", "The sample name"),
        ("crystal_id", "crystalId", "The crystal id for this sample"),
        ("container_id", "containerId", "The container id for this sample"),
        ("location", "location", "The location of this sample within its container"),
        ("dcids", "dcids", "The data collection ids associated with this sample"),
    ),
)
