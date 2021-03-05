import ispyb.model


class ProcessingProgram(ispyb.model.DBCache):
    """An object representing an AutoProcProgram database entry. The object
    lazily accesses the underlying database when necessary and exposes record
    data as python attributes.
    """

    def __init__(self, app_id, db_area, preload=None):
        """Create an ProcessingProgram object for a defined APPID. Requires
        a database data area object exposing further data access methods.

        :param app_id: AutoProcProgramID
        :param db_area: ISPyB database data area object
        :return: An AutoProcProgram object representing the database entry for
                 the specified job AutoProcProgramID
        """
        self._db = db_area
        self._app_id = int(app_id)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError("Don't know the API call for this")

    #   self._data = self._db.retrieve_job(self._app_id)[0]

    @property
    def app_id(self):
        """Returns the AutoProcProgramID."""
        return self._app_id

    @property
    def status_text(self):
        """Returns a human-readable status."""
        if self._data["status"] == 1:
            return "success"
        if self._data["status"] == 0:
            return "failure"
        if self._data["startTime"]:
            return "running"
        return "queued"

    def __repr__(self):
        """Returns an object representation, including the AutoProcProgramID,
        the database connection interface object, and the cache status."""
        return "<AutoProcProgram #%d (%s), %r>" % (
            self._app_id,
            "cached" if self.cached else "uncached",
            self._db,
        )

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "AutoProcProgram #%d (not yet loaded from database)" % self._app_id
        return (
            "\n".join(
                (
                    "AutoProcProgram #{0.app_id}",
                    "  Name         : {0.name}",
                    "  Status       : {0.status_text}",
                    "  Command      : {0.command}",
                    "  Environment  : {0.environment}",
                    "  ProcessingJob: {0.job_id}",
                    "  Defined      : {0.time_defined}",
                    "  Started      : {0.time_start}",
                    "  Last Update  : {0.time_update}",
                    "  Last Message : {0.message}",
                )
            )
        ).format(self)


ispyb.model.add_properties(
    ProcessingProgram,
    (
        ("name", "programs"),
        ("command", "commandLine"),
        ("environment", "environment"),
        ("job_id", "jobId", "Returns the associated ProcessingJob ID (if any)."),
        ("time_defined", "recordTimeStamp"),
        ("time_start", "startTime"),
        ("time_update", "endTime"),
        ("status", "status"),
        ("message", "message"),
    ),
)
