from __future__ import absolute_import, division, print_function

import ispyb
import ispyb.model


class GridInfo(ispyb.model.DBCache):
    """An object representing a GridInfo database entry. The object
    lazily accesses the underlying database when necessary and exposes record
    data as python attributes.
    """

    def __init__(self, dcgid, db_conn, preload=None):
        """Create a GridInfo object for a defined DCGID. Requires
        a database connection object exposing further data access methods.

        :param dcgid: DataCollectionGroupID
        :param db_conn: ISPyB database connection object
        :return: A GridInfo object representing the database entry for
                 the specified DataCollectionGroupID
        """
        self._db = db_conn
        self._dcgid = int(dcgid)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        try:
            self._data = self._db.mx_acquisition.retrieve_dcg_grid(self._dcgid)[0]
        except ispyb.NoResult:
            self._data = None

    @property
    def dcgid(self):
        """Returns the Data Collection Group ID associated with this grid
        information."""
        return self._dcgid

    def __bool__(self):
        """GridInfo object evaluates to True in a boolean context if grid
        information exists in the database. Otherwise it evaluates to False."""
        self.load()
        return self._data is not None

    __nonzero__ = __bool__  # Python 2 compatibility

    def __repr__(self):
        """Returns an object representation, including the DataCollectionGroupID,
        the database connection interface object, and the cache status."""
        return "<GridInfo #%d (%s), %r>" % (
            self._dcgid,
            "cached" if self.cached else "uncached",
            self._db,
        )

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "GridInfo #%d (not yet loaded from database)" % self._dcgid
        return ("\n".join(("GridInfo #{0.dcgid}",))).format(self)


ispyb.model.add_properties(
    GridInfo,
    (
        ("dx_mm", "dx_mm", "Grid element width in mm"),
        ("dy_mm", "dy_mm", "Grid element height in mm"),
        ("id", "gridInfoId", "A unique ID identifying this grid information record"),
        (
            "orientation",
            "orientation",
            'The orientation of the grid, either "horizontal" or "vertical"',
        ),
        (
            "pixels_per_micron_x",
            "pixelsPerMicronX",
            "Number of pixels per micrometre (horizontal) when displaying the grid in GDA",
        ),
        (
            "pixels_per_micron_y",
            "pixelsPerMicronY",
            "Number of pixels per micrometre (vertical) when displaying the grid in GDA",
        ),
        ("timestamp", "recordTimeStamp", "Time and date of record creation"),
        ("steps_x", "steps_x", "Width of the grid scan in number of grid elements"),
        ("steps_y", "steps_y", "Height of the grid scan in number of grid elements"),
        (
            "snaked",
            "snaked",
            "Whether the fast scan axis is inverted (1) or kept (0) for every slow axis acquisition",
        ),
        (
            "snapshot_offset_pixel_x",
            "snapshot_offsetXPixel",
            "Horizontal distance from the top left corner in GDA to the first grid element",
        ),
        (
            "snapshot_offset_pixel_y",
            "snapshot_offsetYPixel",
            "Vertical distance from the top left corner in GDA to the first grid element",
        ),
    ),
)
