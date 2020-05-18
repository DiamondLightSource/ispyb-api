from __future__ import absolute_import, division, print_function

import ispyb
import ispyb.model


class Detector(ispyb.model.DBCache):
    """An object representing a Detector database entry. The object
    lazily accesses the underlying database when necessary and exposes record
    data as python attributes.
    """

    def __init__(self, detectorid, db_conn, preload=None):
        """Create a Detector object for a defined detectorid. Requires
        a database connection object exposing further data access methods.

        :param detectorid: detectorId
        :param db_conn: ISPyB database connection object
        :return: A Detector object representing the database entry for
                 the specified detectorId
        """
        self._db = db_conn
        self._detectorid = int(detectorid)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def id(self):
        "Returns the detectorId"
        return self._detectorid

    def __repr__(self):
        """Returns an object representation, including the DetectorID,
        the database connection interface object, and the cache status."""
        return "<Detector #%d (%s), %r>" % (
            self._detectorid,
            "cached" if self.cached else "uncached",
            self._db,
        )

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return "Detector id: %d (not yet loaded from database)" % (self._detectorid)
        return (
            "\n".join(
                (
                    "Detector",
                    "  id                    : {0.id}",
                    "  manufacturer          : {0.manufacturer}",
                    "  model                 : {0.model}",
                    "  serial_number         : {0.serial_number}",
                    "  pixel_size_horizontal : {0.pixel_size_horizontal}",
                    "  pixel_size_vertical   : {0.pixel_size_vertical}",
                    "  pixels_x              : {0.pixels_x}",
                    "  pixels_y              : {0.pixels_y}",
                    "  distance_min          : {0.distance_min}",
                    "  distance_max          : {0.distance_max}",
                )
            )
        ).format(self)


ispyb.model.add_properties(
    Detector,
    (
        ("type", "detectorType"),
        ("manufacturer", "detectorManufacturer"),
        ("model", "detectorModel"),
        ("pixel_size_horizontal", "detectorPixelSizeHorizontal"),
        ("pixel_size_vertical", "detectorPixelSizeVertical"),
        ("serial_number", "detectorSerialNumber"),
        ("distance_min", "detectorDistanceMin"),
        ("distance_max", "detectorDistanceMax"),
        ("sensor_thickness", "sensorThickness"),
        ("pixels_x", "numberOfPixelsX"),
        ("pixels_y", "numberOfPixelsY"),
    ),
)
