import tabulate

import ispyb.model


class ImageQualityIndicators(ispyb.model.DBCache):
    """An object representing an ImageQualityIndicators database entry.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, dcid, image_number, db_conn, preload=None):
        """Create an ImageQualityIndicators object for a given combination of
        DataCollectionId and ImageNumber.

        Requires a database connection object exposing further data access
        methods.

        :param dcid: DataCollectionId
        :param image_number: ImageNumber
        :param db_conn: ISPyB database connection object
        :return: An ImageQualityIndicators object representing the database
                 entry for the specified DataCollectionId and ImageNumber
        """
        self._db = db_conn
        self._dcid = int(dcid)
        self._image_number = int(image_number)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def dcid(self):
        """Returns the DataCollectionId."""
        return self._dcid

    @property
    def image_number(self):
        """Returns the ImageNumber."""
        return self._image_number

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if not self.cached:
            return (
                "ImageQualityIndicators dcid: %d, imageNumber: %d (not yet loaded from database)"
                % (self._dcid, self._image_number)
            )
        return (
            "\n".join(
                (
                    "ImageQualityIndicators",
                    "  dcid                    : {0.dcid}",
                    "  image_number            : {0.image_number}",
                    "  spot_count              : {0.spot_count}",
                    "  bragg_candidates        : {0.bragg_candidates}",
                    "  resolution_method_1     : {0.resolution_method_1}",
                    "  resolution_method_2     : {0.resolution_method_2}",
                    "  total_integrated_signal : {0.total_integrated_signal}",
                )
            )
        ).format(self)


ispyb.model.add_properties(
    ImageQualityIndicators,
    (
        ("spot_count", "spotTotal"),
        ("bragg_candidates", "goodBraggCandidates"),
        ("resolution_method_1", "method1Res"),
        ("resolution_method_2", "method2Res"),
        ("total_integrated_signal", "totalIntegratedSignal"),
    ),
)

import collections


class ImageQualityIndicatorsList(ispyb.model.DBCache, collections.Sequence):
    """An object representing a list of  ImageQualityIndicators database entries.
    The object lazily accesses the underlying database when necessary and
    exposes record data as python attributes.
    """

    def __init__(self, dcid, db_conn, preload=None):
        """Create an ImageQualityIndicators object for a given combination of
        DataCollectionId and ImageNumber.

        Requires a database connection object exposing further data access
        methods.

        :param dcid: DataCollectionId
        :param image_number: ImageNumber
        :param db_conn: ISPyB database connection object
        :return: An ImageQualityIndicators object representing the database
                 entry for the specified DataCollectionId and ImageNumber
        """
        self._db = db_conn
        self._dcid = int(dcid)
        if preload:
            self._data = preload

    def reload(self):
        """Load/update information from the database."""
        raise NotImplementedError()

    @property
    def dcid(self):
        """Returns the DataCollectionId."""
        return self._dcid

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        data = self._data[i]
        return ImageQualityIndicators(
            self._dcid, data["imageNumber"], self._db, preload=data
        )

    def __str__(self):
        """Returns a pretty-printed object representation."""
        headers = (
            "dcid",
            "image_number",
            "spot_count",
            "bragg_candidates",
            "resolution_method_1",
            "resolution_method_2",
            "total_integrated_signal",
        )
        rows = []
        for qi in self:
            rows.append([getattr(qi, k) for k in headers])
        return tabulate.tabulate(rows, headers=headers, tablefmt="psql")
