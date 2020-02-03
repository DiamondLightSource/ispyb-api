from __future__ import absolute_import, division, print_function

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
