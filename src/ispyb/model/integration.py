import ispyb.model
import ispyb.model.processingprogram


class IntegrationResult(ispyb.model.DBCache):
    """An object representing a data collection integration result database entry.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, apiid, db_conn, preload=None):
        """Create a IntegrationResult object for a defined AutoProcIntegrationID.
        Requires a database connection object exposing further data access
        methods.

        :param apiid: AutoProcIntegrationID
        :param db_conn: ISPyB database connection object
        :return: An IntegrationResult object representing the database entry for
                 the specified AutoProcIntegrationID
        """
        self._cache_dc = None
        self._cache_app = None
        self._db = db_conn
        self._apiid = int(apiid)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError("TODO: Not implemented yet")

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
        if self._cache_dc is None:
            if self.DCID is None:
                return None
            self._cache_dc = self._db.get_data_collection(self.DCID)
        return self._cache_dc

    @property
    def unit_cell(self):
        """Returns the unit cell model"""
        return ispyb.model.integration.UnitCell(
            self._data["cell_a"],
            self._data["cell_b"],
            self._data["cell_c"],
            self._data["cell_alpha"],
            self._data["cell_beta"],
            self._data["cell_gamma"],
        )

    @property
    def APIID(self):
        """Returns the AutoProcIntegrationID."""
        return self._apiid

    @property
    def program(self):
        """Returns the AutoProcProgram model object for the processing program
        responsible for this integration result."""
        if self._cache_app is None:
            self._cache_app = ispyb.model.processingprogram.ProcessingProgram(
                self.APPID, self._db
            )
        return self._cache_app

    def __repr__(self):
        """Returns an object representation, including the AutoProcIntegrationID,
        the database connection interface object, and the cache status."""
        return "<IntegrationResult #%d (%s), %r>" % (
            self._apiid,
            "cached" if self.cached else "uncached",
            self._db,
        )

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "IntegrationResult #%d (not yet loaded from database)" % self._apiid
        return (
            "\n".join(
                (
                    "IntegrationResult #{ir.APIID}",
                    "  DCID             : {ir.DCID}",
                    "  APPID            : {ir.APPID}",
                    "  Start Image      : {ir.image_start}",
                    "  End Image        : {ir.image_end}",
                    "  Detector Distance: {ir.detector_distance}",
                    "  Timestamp        : {ir.timestamp}",
                )
            )
        ).format(ir=self)


ispyb.model.add_properties(
    IntegrationResult,
    (
        ("APPID", "autoProcProgramId"),
        ("image_start", "startImageNumber"),
        ("image_end", "endImageNumber"),
        ("detector_distance", "refinedDetectorDistance"),
        ("timestamp", "recordTimeStamp"),
    ),
)


class UnitCell:
    """A read-only object representing the parameters of the unit cell,
    ie. edges and angles.
    """

    def __init__(self, a, b, c, alpha, beta, gamma):
        """Unit cell object

        :param a: Edge a in Angstrom
        :param b: Edge b in Angstrom
        :param c: Edge c in Angstrom
        :param alpha: Angle alpha
        :param beta: Angle beta
        :param gamma: Angle gamma
        :return: A UnitCell object
        """
        self._a = a
        self._b = b
        self._c = c
        self._alpha = alpha
        self._beta = beta
        self._gamma = gamma

    @property
    def a(self):
        """Returns dimension a of unit cell in Angstroms"""
        return self._a

    @property
    def b(self):
        """Returns dimension b of unit cell in Angstroms"""
        return self._b

    @property
    def c(self):
        """Returns dimension c of unit cell in Angstroms"""
        return self._c

    @property
    def alpha(self):
        """Returns angle alpha of unit cell"""
        return self._alpha

    @property
    def beta(self):
        """Returns angle beta of unit cell"""
        return self._beta

    @property
    def gamma(self):
        """Returns angle gamma of unit cell"""
        return self._gamma

    def __str__(self):
        """Returns a pretty-printed object representation."""
        return (
            "\n".join(
                (
                    "  a         : {uc.a}",
                    "  b         : {uc.b}",
                    "  c         : {uc.c}",
                    "  alpha     : {uc.alpha}",
                    "  beta      : {uc.beta}",
                    "  gamma     : {uc.gamma}",
                )
            )
        ).format(uc=self)
