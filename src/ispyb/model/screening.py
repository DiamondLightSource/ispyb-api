import ispyb.model
from ispyb.model.integration import UnitCell


class Screening(ispyb.model.DBCache):
    """An object representing a Screening database entry.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, screening_id, db_conn, preload=None):
        """Create a Screening object for a defined ScreeningId.

        Requires a database connection object exposing further data access
        methods.

        :param sceening_id: ScreeningId
        :param db_conn: ISPyB database connection object
        :return: A Screening object representing the database entry for
                 the specified ScreeningId
        """
        self._db = db_conn
        self._screening_id = int(screening_id)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def screening_id(self):
        """Returns the ScreeningId."""
        return self._screening_id

    @property
    def outputs(self):
        """Returns the list of ScreeningOutput objects associated with this
        database entry."""
        raise NotImplementedError()

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "Screening #%d (not yet loaded from database)" % self._screening_id
        return (
            "\n".join(
                (
                    "Screening #{0.screening_id}",
                    "  comment         : {0.comment}",
                    "  short_comment   : {0.short_comment}",
                    "  program         : {0.program}",
                )
            )
        ).format(self)


ispyb.model.add_properties(
    Screening,
    (
        ("comment", "comments"),
        ("short_comment", "shortComments"),
        ("program", "programVersion"),
    ),
)


class ScreeningOutput(ispyb.model.DBCache):
    """An object representing a ScreeningOutput database entry.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, output_id, db_conn, preload=None):
        """Create a ScreeningOutput object for a defined ScreeningOutputId.

        Requires a database connection object exposing further data access
        methods.

        :param output_id: ScreeningOutputId
        :param db_conn: ISPyB database connection object
        :return: A ScreeningOutput object representing the database entry for
                 the specified ScreeningOutputId
        """
        self._db = db_conn
        self._output_id = output_id
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def output_id(self):
        """Returns the ScreeningOutputId."""
        return self._output_id

    @property
    def lattices(self):
        """Returns the list of ScreeningOutputLattice objects associated with
        this database entry."""
        raise NotImplementedError()

    @property
    def strategies(self):
        """Returns the list of ScreeningStrategy objects associated with this
        database entry."""
        raise NotImplementedError()

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return (
                "ScreeningOutput #%d (not yet loaded from database)" % self._output_id
            )
        return (
            "\n".join(
                (
                    "ScreeningOutput #{0.output_id}",
                    "  alignment_success  : {0.alignment_success}",
                    "  indexing_success   : {0.indexing_success}",
                    "  strategy_success   : {0.strategy_success}",
                    "  program            : {0.program}",
                )
            )
        ).format(self)


ispyb.model.add_properties(
    ScreeningOutput,
    (
        ("alignment_success", "alignmentSuccess"),
        ("indexing_success", "indexingSuccess"),
        ("strategy_success", "strategySuccess"),
        ("program", "program"),
    ),
)


class ScreeningOutputLattice(ispyb.model.DBCache):
    """An object representing a ScreeningOutputLattice database entry.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, lattice_id, db_conn, preload=None):
        """Create a ScreeningOutputLattice object for a defined ScreeningOutputLatticeId.

        Requires a database connection object exposing further data access
        methods.

        :param lattice_id: ScreeningOutputLatticeId
        :param db_conn: ISPyB database connection object
        :return: A ScreeningOutputLattice object representing the database entry
                 for the specified ScreeningOutputLatticeId
        """
        self._db = db_conn
        self._lattice_id = lattice_id
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def lattice_id(self):
        """Returns the ScreeningOutputLatticeId."""
        return self._lattice_id

    @property
    def unit_cell(self):
        """Returns the unit cell model."""
        return UnitCell(
            self._data["unitCell_a"],
            self._data["unitCell_b"],
            self._data["unitCell_c"],
            self._data["unitCell_alpha"],
            self._data["unitCell_beta"],
            self._data["unitCell_gamma"],
        )

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return (
                "ScreeningOutputLattice #%d (not yet loaded from database)"
                % self._lattice_id
            )
        return (
            "\n".join(
                (
                    "ScreeningOutputLattice #{0.lattice_id}",
                    "  spacegroup  : {0.spacegroup}",
                    "{0.unit_cell}",
                )
            )
        ).format(self)


ispyb.model.add_properties(ScreeningOutputLattice, (("spacegroup", "spaceGroup"),))


class ScreeningStrategy(ispyb.model.DBCache):
    """An object representing a ScreeningStrategy database entry.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, strategy_id, db_conn, preload=None):
        """Create a ScreeningStrategy object for a defined ScreeningStrategyId.

        Requires a database connection object exposing further data access
        methods.

        :param strategy_id: ScreeningStrategyId
        :param db_conn: ISPyB database connection object
        :return: A ScreeningStrategy object representing the database entry for
                 the specified ScreeningStrategyId
        """
        self._db = db_conn
        self._strategy_id = strategy_id
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def strategy_id(self):
        """Returns the ScreeningStrategyId."""
        return self._strategy_id

    @property
    def wedges(self):
        """Returns the list of ScreeningStrategyWedge objects associated with
        this database entry."""
        raise NotImplementedError()

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return (
                "ScreeningStrategy #%d (not yet loaded from database)"
                % self._strategy_id
            )
        return (
            "\n".join(
                (
                    "ScreeningStrategy #{0.strategy_id}",
                    "  anomalous           : {0.anomalous}",
                    "  exposure_time       : {0.exposure_time}",
                    "  program             : {0.program}",
                    "  ranking_resolution  : {0.ranking_resolution}",
                )
            )
        ).format(self)


ispyb.model.add_properties(
    ScreeningStrategy,
    (
        ("anomalous", "anomalous"),
        ("exposure_time", "exposureTime"),
        ("program", "program"),
        ("ranking_resolution", "rankingResolution"),
    ),
)


class ScreeningStrategyWedge(ispyb.model.DBCache):
    """An object representing a ScreeningStrategyWedge database entry.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, wedge_id, db_conn, preload=None):
        """Create a ScreeningStrategyWedge object for a defined ScreeningStrategyWedgeId.

        Requires a database connection object exposing further data access
        methods.

        :param strategy_wedge_id: ScreeningStrategyWedgeId
        :param db_conn: ISPyB database connection object
        :return: A ScreeningStrategyWedge object representing the database entry
                 for the specified ScreeningStrategyWedgeId
        """
        self._db = db_conn
        self._wedge_id = wedge_id
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def wedge_id(self):
        """Returns the ScreeningStrategyWedgeId."""
        return self._wedge_id

    @property
    def sub_wedges(self):
        """Returns the list of ScreeningStrategySubWedge objects associated with
        this database entry."""
        raise NotImplementedError()

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return (
                "ScreeningStrategyWedge #%d (not yet loaded from database)"
                % self._wedge_id
            )
        return (
            "\n".join(
                (
                    "ScreeningStrategyWedge #{0.wedge_id}",
                    "  chi               : {0.chi}",
                    "  kappa             : {0.kappa}",
                    "  phi               : {0.phi}",
                    "  completeness      : {0.completeness}",
                    "  multiplicity      : {0.multiplicity}",
                    "  number_of_images  : {0.number_of_images}",
                    "  resolution        : {0.resolution}",
                    "  wedge_number      : {0.wedge_number}",
                )
            )
        ).format(self)


ispyb.model.add_properties(
    ScreeningStrategyWedge,
    (
        ("chi", "chi"),
        ("completeness", "completeness"),
        ("kappa", "kappa"),
        ("multiplicity", "multiplicity"),
        ("number_of_images", "numberOfImages"),
        ("phi", "phi"),
        ("resolution", "resolution"),
        ("wedge_number", "wedgeNumber"),
    ),
)


class ScreeningStrategySubWedge(ispyb.model.DBCache):
    """An object representing a ScreeningStrategySubWedge database entry.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, sub_wedge_id, db_conn, preload=None):
        """Create a ScreeningStrategySubWedge object for a defined ScreeningStrategySubWedgeId.

        Requires a database connection object exposing further data access
        methods.

        :param strategy_sub_wedge_id: ScreeningStrategySubWedgeId
        :param db_conn: ISPyB database connection object
        :return: A ScreeningStrategySubWedge object representing the database entry
                 for the specified ScreeningStrategySubWedgeId
        """
        self._db = db_conn
        self._sub_wedge_id = sub_wedge_id
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def sub_wedge_id(self):
        """Returns the ScreeningStrategySubWedgeId."""
        return self._sub_wedge_id

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return (
                "ScreeningStrategySubWedge #%d (not yet loaded from database)"
                % self._sub_wedge_id
            )
        return (
            "\n".join(
                (
                    "ScreeningStrategySubWedge #{0.sub_wedge_id}",
                    "  axis_end           : {0.axis_end}",
                    "  axis_start         : {0.axis_start}",
                    "  completeness       : {0.completeness}",
                    "  exposure_time      : {0.exposure_time}",
                    "  multiplicity       : {0.multiplicity}",
                    "  number_of_images   : {0.number_of_images}",
                    "  oscillation_range  : {0.oscillation_range}",
                    "  resolution         : {0.resolution}",
                    "  rotation_axis      : {0.rotation_axis}",
                    "  transmission       : {0.transmission}",
                    "  sub_wedge_number   : {0.sub_wedge_number}",
                )
            )
        ).format(self)


ispyb.model.add_properties(
    ScreeningStrategySubWedge,
    (
        ("axis_end", "axisEnd"),
        ("axis_start", "axisStart"),
        ("completeness", "completeness"),
        ("exposure_time", "exposureTime"),
        ("multiplicity", "multiplicity"),
        ("number_of_images", "numberOfImages"),
        ("oscillation_range", "oscillationRange"),
        ("resolution", "resolution"),
        ("rotation_axis", "rotationAxis"),
        ("sub_wedge_number", "subWedgeNumber"),
        ("transmission", "transmission"),
    ),
)
