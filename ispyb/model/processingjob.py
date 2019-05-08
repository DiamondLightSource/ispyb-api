from __future__ import absolute_import, division, print_function

import collections

import ispyb.model
import ispyb.model.processingprogram


class ProcessingJob(ispyb.model.DBCache):
    """An object representing a ProcessingJob database entry. The object lazily
    accesses the underlying database when necessary and exposes record data
    as python attributes.
    """

    def __init__(self, jobid, db_area):
        """Create a ProcessingJob object for a defined ProcessingJob ID. Requires
        a database data area object exposing further data access methods.

        :param jobid: ProcessingJob ID
        :param db_area: ISPyB database data area object
        :return: A ProcessingJob object representing the database entry for the
                 specified job ID
        """
        self._cache_dc = None
        self._cache_parameters = None
        self._cache_programs = None
        self._cache_sweeps = None
        self._db = db_area
        self._jobid = int(jobid)

    def __eq__(self, other):
        """Equality of the model object depends on the equality of the
        underlying database reference."""
        if not isinstance(other, ProcessingJob):
            return False
        return self._jobid == other._jobid and self._db == other._db

    def __ne__(self, other):
        """Test for non-equality. Implementation required for Python 2."""
        return not self.__eq__(other)

    def __hash__(self):
        """Generates a 'unique' hash value for the object."""
        return hash(("ProcessingJob", self._db, self._jobid))

    def reload(self):
        """Load/update information from the database."""
        self._data = self._db.retrieve_job(self._jobid)[0]

    @property
    def DCID(self):
        """Returns the main data collection id."""
        dcid = self._data["dataCollectionId"]
        if dcid is None:
            return None
        return int(dcid)

    @property
    def data_collection(self):
        """Returns the DataCollection model object for the main data collection of
        the ProcessingJob."""
        dcid = self._data["dataCollectionId"]
        if dcid is None:
            return None
        if self._cache_dc is None:
            self._cache_dc = self._db.conn.get_data_collection(
                self._data["dataCollectionId"]
            )
        return self._cache_dc

    @property
    def jobid(self):
        """Returns the ProcessingJob ID."""
        return self._jobid

    @property
    def automatic(self):
        """Returns whether this processing job was initiated as part of automatic
        data processing."""
        return bool(self._data["automatic"])

    @property
    def parameters(self):
        if self._cache_parameters is None:
            self._cache_parameters = ProcessingJobParameters(self._jobid, self._db)
        return self._cache_parameters

    @property
    def sweeps(self):
        """Returns a list of ProcessingJobImageSweeps involved in this
        processing job."""
        if self._cache_sweeps is None:
            self._cache_sweeps = ProcessingJobImageSweeps(self._jobid, self._db)
        return self._cache_sweeps

    @property
    def programs(self):
        if self._cache_programs is None:
            self._cache_programs = ProcessingJobPrograms(self._jobid, self._db)
        return self._cache_programs

    def __repr__(self):
        """Returns an object representation, including the processing job ID,
        the database connection interface object, and the cache status."""
        return "<ProcessingJob #%d (%s), %r>" % (
            self._jobid,
            "cached" if self.cached else "uncached",
            self._db,
        )

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "ProcessingJob #%d (not yet loaded from database)" % self._jobid
        return (
            "\n".join(
                (
                    "ProcessingJob #{pj.jobid}",
                    "  Name        : {pj.name}",
                    "  Recipe      : {pj.recipe}",
                    "  Comments    : {pj.comment}",
                    "  Primary DCID: {pj.DCID}",
                    "  Timestamp   : {pj.timestamp}",
                )
            )
        ).format(pj=self)


ispyb.model.add_properties(
    ProcessingJob,
    (
        ("name", "displayName"),
        ("comment", "comments"),
        ("recipe", "recipe"),
        ("timestamp", "recordTimestamp"),
    ),
)


class ProcessingJobParameterValue(ispyb.model.EncapsulatedValue):
    """An object representing a key/value parameter pair. The object behaves like
    the value string, but also contains a .key and .parameter_id attribute.
    """

    def __init__(self, key, value, parameter_id):
        ispyb.model.EncapsulatedValue.__init__(self, value)
        self._key, self._pid = key, parameter_id

    @property
    def key(self):
        """Returns the parameterKey"""
        return self._key

    @property
    def parameter_id(self):
        """Returns the processingJobParameterId"""
        return self._pid

    def __repr__(self):
        """Returns an object representation, including the processing job parameter
        key, value, and ID."""
        return "ProcessingJobParameterValue(key:%r, value:%r, id:%r)" % (
            self._key,
            self._value,
            self._pid,
        )


class ProcessingJobParameters(ispyb.model.DBCache):
    """An object representing the parameters for a ProcessingJob database entry.
    The object lazily accesses the underlying database when necessary and
    exposes the parameters both as a list and in a dictionary-like fashion.
    """

    def __init__(self, jobid, db_area):
        """Create a ProcessingJobParameters object for a defined ProcessingJob ID.
        Requires a database data area object exposing further data access
        methods.

        :param jobid: ProcessingJob ID
        :param db_area: ISPyB database data area object
        :return: A ProcessingJobParameters object representing the database
                 entries for the parameters of the specified job ID
        """
        self._db = db_area
        self._jobid = int(jobid)

    def reload(self):
        """Load/update information from the database."""
        try:
            self._data = [
                (
                    p["parameterKey"],
                    ProcessingJobParameterValue(
                        p["parameterKey"], p["parameterValue"], p["parameterId"]
                    ),
                )
                for p in self._db.retrieve_job_parameters(self._jobid)
            ]
        except ispyb.NoResult:
            self._data = []
        self._data_dict = collections.OrderedDict(self._data)

    def __getitem__(self, item):
        """Allow accessing the parameter records as a list or dictionary."""
        try:
            # Assume 'item' is an integer: treat as list
            return self._data[item]
        except TypeError:
            # Assume 'item' is a key: treat as dictionary
            return self._data_dict[item]

    def __len__(self):
        """Return the number of parameters attached to this processing job."""
        return len(self._data)

    def __repr__(self):
        """Returns an object representation, including the processing job ID,
        the database connection interface object, and the cache status."""
        return "<ProcessingJobParameters #%d (%s), %r>" % (
            self._jobid,
            "cached" if self.cached else "uncached",
            self._db,
        )


class ProcessingJobImageSweep(object):
    """An object representing an image sweep for a processing job. Each image
    sweep has a data collection id, a start and an end image, and an image
    sweep id.
    """

    def __init__(self, dcid, start, end, sweep_id, db_area):
        self._dcid, self._sid = int(dcid), int(sweep_id)
        self._start, self._end = int(start), int(end)
        self._db = db_area

    @property
    def DCID(self):
        """Returns the data collection id."""
        return self._dcid

    @property
    def data_collection(self):
        """Returns the DataCollection model object for the data collection of this
        sweep."""
        return self._db.conn.get_data_collection(self._dcid)

    @property
    def start(self):
        """Returns the start image number of the sweep"""
        return self._start

    @property
    def end(self):
        """Returns the end image number of the sweep"""
        return self._end

    @property
    def sweep_id(self):
        """Returns the processingJobImageSweepId"""
        return self._sid

    def __repr__(self):
        """Returns an object representation, including all contained attribute
        values."""
        return "ProcessingJobImageSweep(dcid:%r, start:%r, end:%r, id:%r)" % (
            self._dcid,
            self._start,
            self._end,
            self._sid,
        )


class ProcessingJobImageSweeps(ispyb.model.DBCache):
    """An object representing the list of image sweeps for a ProcessingJob
    database entry. The object lazily accesses the underlying database when
    necessary and exposes the sweeps as a list.
    """

    def __init__(self, jobid, db_area):
        """Create a ProcessingJobImageSweeps object for a defined ProcessingJob ID.
        Requires a database data area object exposing further data access
        methods.

        :param jobid: ProcessingJob ID
        :param db_area: ISPyB database data area object
        :return: A ProcessingJobImageSweeps object representing the database
                 entries for the sweeps of the specified job ID
        """
        self._db = db_area
        self._jobid = int(jobid)

    def reload(self):
        """Load/update information from the database."""
        try:
            self._data = [
                ProcessingJobImageSweep(
                    p["dataCollectionId"],
                    p["startImage"],
                    p["endImage"],
                    p["sweepId"],
                    self._db,
                )
                for p in self._db.retrieve_job_image_sweeps(self._jobid)
            ]
        except ispyb.NoResult:
            self._data = []

    def __getitem__(self, item):
        """Allow accessing the sweep records as a list."""
        return self._data[item]

    def __len__(self):
        """Return the number of sweeps attached to this processing job."""
        return len(self._data)

    def __repr__(self):
        """Returns an object representation, including the processing job ID,
        the database connection interface object, and the cache status."""
        return "<ProcessingJobImageSweeps #%d (%s), %r>" % (
            self._jobid,
            "cached" if self.cached else "uncached",
            self._db,
        )


class ProcessingJobPrograms(ispyb.model.DBCache):
    """An object representing the programs working on a ProcessingJob.
    The object lazily accesses the underlying database when
    necessary and exposes the programs as a list of AutoProcProgam objects.
    """

    def __init__(self, jobid, db_area):
        """Create a ProcessingJobPrograms object for a defined ProcessingJob ID.
        Requires a database data area object exposing further data access
        methods.

        :param jobid: ProcessingJob ID
        :param db_area: ISPyB database data area object
        :return: A ProcessingJobPrograms object representing the database
                 entries for the programs working on the specified job ID.
        """
        self._db = db_area
        self._jobid = int(jobid)

    def reload(self):
        """Load/update information from the database."""
        try:
            self._data = [
                ispyb.model.processingprogram.ProcessingProgram(
                    p["id"], self._db, preload=p
                )
                for p in self._db.retrieve_programs_for_job_id(self._jobid)
            ]
        except ispyb.NoResult:
            self._data = []

    def __getitem__(self, item):
        """Allow accessing the program records as a list."""
        return self._data[item]

    def __len__(self):
        """Return the number of programs attached to this processing job."""
        return len(self._data)

    def __repr__(self):
        """Returns an object representation, including the processing job ID,
        the database connection interface object, and the cache status."""
        return "<ProcessingJobPrograms #%d (%s), %r>" % (
            self._jobid,
            "cached" if self.cached else "uncached",
            self._db,
        )
