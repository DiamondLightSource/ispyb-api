import ispyb.model


class SampleGroup(ispyb.model.DBCache):
    def __init__(self, sample_group_id, db_conn, preload=None):
        """Create a SampleGroup object for a defined sample_group_id. Requires
        a database connection object exposing further data access methods.

        :param sample_group_id: bLSampleGroupId
        :param db_conn: ISPyB database connection object
        :return: A SampleGroup object representing the database entry for
                 the specified bLSampleGroupId
        """
        self._db = db_conn
        self._id = int(sample_group_id)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def id(self):
        "Returns the detectorId"
        return self._id

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "SampleGroup #%d (not yet loaded from database)" % self._id
        return (
            "\n".join(
                (
                    "SampleGroup #%s" % self._id,
                    "  Name       : %s" % self.name,
                    "  Sample ids : %s"
                    % (
                        ",".join(str(i) for i in self.sample_ids)
                        if self.sample_ids
                        else "None"
                    ),
                    "  DCIDs      : %s"
                    % (",".join(str(i) for i in self.dcids) if self.dcids else "None"),
                )
            )
        ).format(self)


ispyb.model.add_properties(
    SampleGroup,
    (
        ("name", "name", "The SampleGroup name"),
        ("sample_ids", "sample_ids", "The sample ids comprising the sample group"),
        ("dcids", "dcids", "The data collection ids associated with this sample group"),
    ),
)
