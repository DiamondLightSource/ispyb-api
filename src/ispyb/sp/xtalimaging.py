from ispyb.interface.dataarea import DataArea


class XtalImaging(DataArea):
    """provides methods for accessing crystal imaging tables."""

    def upsert_sample_image(
        self,
        id=None,
        sample_id=None,
        inspection_id=None,
        microns_per_pixel_x=None,
        microns_per_pixel_y=None,
        image_full_path=None,
        comments=None,
    ):
        """Store new or update existing sample image.

        :param image_full_path: The full path to the sample image
        :return: The sample_image_id.
        """
        return self.get_connection().call_sp_write(
            procname="upsert_sample_image",
            args=[
                id,
                sample_id,
                inspection_id,
                microns_per_pixel_x,
                microns_per_pixel_y,
                image_full_path,
                comments,
            ],
        )

    def upsert_sample_image_auto_score(
        self, image_full_path, schema_name, score_class, probability
    ):
        """Store new or update existing automatic score for a sample image.

        :param image_full_path: The full path to the sample image
        :param schema_name: The name of the scoring schema, e.g. MARCO
        :param score_class: A string that describes the thing we're scoring, e.g. crystal, clear, precipitant, other
        :param probability: A float indicating the probability that the image contains the score_class
        """
        self.get_connection().call_sp_write(
            procname="upsert_sample_image_auto_score",
            args=[image_full_path, schema_name, score_class, probability],
        )

    def insert_subsample_for_image_full_path(
        self,
        image_full_path,
        source,
        position1x,
        position1y,
        position2x=None,
        position2y=None,
        experiment_type=None,
    ):
        """Store new subsample for a given sample image.

        Either specify a point (by providing position1x and position1y)
        or a ROI box (by additionally providing position2x and position2y).
        Position coordinates are given in pixels from the top-left corner
        of the image.

        :param image_full_path: The full path to the sample image
        :type image_full_path: str
        :param source: manual or auto
        :type source: str
        :param position1x: x component of position1
        :type position1x: int
        :param position1y: y component of position1
        :type position1y: int
        :param position2x: x component of position2 which is the lower right
        corner of a ROI box
        :type position2x: int
        :param position2y: y component of position2 which is the lower right
        corner of a ROI box
        :type position2y: int
        :return: The subsample_id.
        """
        id = None
        return self.get_connection().call_sp_write(
            procname="insert_subsample_for_image_full_path_v2",
            args=[
                id,
                image_full_path,
                source,
                position1x,
                position1y,
                position2x,
                position2y,
                experiment_type,
            ],
        )

    def retrieve_container_for_barcode(self, barcode):
        """Retrieve info about the container indetified by the give barcode."""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_container_for_barcode", args=[barcode]
        )

    def retrieve_container_for_inspection_id(self, inspection_id):
        """Retrieve info about the container identified by container inspection ID"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_container_for_inspection_id", args=[inspection_id]
        )

    def retrieve_sample_for_container_id_and_location(self, container_id, location):
        """Retrieve info about the sample identified by the given container ID and its location."""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_sample_for_container_id_and_location",
            args=[container_id, location],
        )
