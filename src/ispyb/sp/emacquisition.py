# emacquisition.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2014-09-24
#
# Methods to store EM acquisition data
#

import copy

from ispyb.sp.acquisition import Acquisition
from ispyb.strictordereddict import StrictOrderedDict


class EMAcquisition(Acquisition):
    """EMAcquisition provides methods to store data in the MotionCorrection and CTF tables."""

    def __init__(self):
        self.insert_data_collection_group = super().upsert_data_collection_group
        self.insert_data_collection = super().upsert_data_collection
        self.update_data_collection_group = super().upsert_data_collection_group
        self.update_data_collection = super().upsert_data_collection

    _movie_params = StrictOrderedDict(
        [
            ("movieId", None),
            ("dataCollectionId", None),
            ("movieNumber", None),
            ("movieFullPath", None),
            ("createdTimeStamp", None),
            ("positionX", None),
            ("positionY", None),
            ("nominalDefocus", None),
        ]
    )

    _motion_correction_drift_params = StrictOrderedDict(
        [
            ("motionCorrectionDriftId", None),
            ("motionCorrectionId", None),
            ("frameNumber", None),
            ("deltaX", None),
            ("deltaY", None),
        ]
    )

    @classmethod
    def get_movie_params(cls):
        return copy.deepcopy(cls._movie_params)

    @classmethod
    def get_motion_correction_drift_params(cls):
        return copy.deepcopy(cls._motion_correction_drift_params)

    def insert_movie(self, values):
        """Store new movie params."""
        return self.get_connection().call_sp_write(procname="upsert_movie", args=values)

    def insert_motion_correction(
        self,
        motion_correction_id=None,
        movie_id=None,
        auto_proc_program_id=None,
        image_number=None,
        first_frame=None,
        last_frame=None,
        dose_per_frame=None,
        total_motion=None,
        average_motion_per_frame=None,
        drift_plot_full_path=None,
        micrograph_full_path=None,
        micrograph_snapshot_full_path=None,
        fft_full_path=None,
        fft_corrected_full_path=None,
        patches_used_x=None,
        patches_used_y=None,
        comments=None,
    ):
        """Store new motion correction parameters."""
        return self.get_connection().call_sp_write(
            procname="upsert_motion_correction",
            args=(
                motion_correction_id,
                movie_id,
                auto_proc_program_id,
                image_number,
                first_frame,
                last_frame,
                dose_per_frame,
                total_motion,
                average_motion_per_frame,
                drift_plot_full_path,
                micrograph_full_path,
                micrograph_snapshot_full_path,
                fft_full_path,
                fft_corrected_full_path,
                patches_used_x,
                patches_used_y,
                comments,
            ),
        )

    def insert_ctf(
        self,
        ctf_id=None,
        motion_correction_id=None,
        auto_proc_program_id=None,
        box_size_x=None,
        box_size_y=None,
        min_resolution=None,
        max_resolution=None,
        min_defocus=None,
        max_defocus=None,
        defocus_step_size=None,
        astigmatism=None,
        astigmatism_angle=None,
        estimated_resolution=None,
        estimated_defocus=None,
        amplitude_contrast=None,
        cc_value=None,
        fft_theoretical_full_path=None,
        comments=None,
    ):
        """Store new contrast transfer function parameters."""
        return self.get_connection().call_sp_write(
            procname="upsert_ctf",
            args=(
                ctf_id,
                motion_correction_id,
                auto_proc_program_id,
                box_size_x,
                box_size_y,
                min_resolution,
                max_resolution,
                min_defocus,
                max_defocus,
                defocus_step_size,
                astigmatism,
                astigmatism_angle,
                estimated_resolution,
                estimated_defocus,
                amplitude_contrast,
                cc_value,
                fft_theoretical_full_path,
                comments,
            ),
        )

    def insert_motion_correction_drift(self, values):
        """Store new motion correction drift params."""
        return self.get_connection().call_sp_write(
            procname="upsert_motion_correction_drift", args=values
        )

    def insert_particle_picker(
        self,
        particle_picker_id=None,
        first_motion_correction_id=None,
        auto_proc_program_id=None,
        particle_picking_template=None,
        particle_diameter=None,
        number_of_particles=None,
        summary_image_full_path=None,
    ):
        """Store new particle picker parameters."""
        return self.get_connection().call_sp_write(
            procname="upsert_particle_picker_v2",
            args=(
                particle_picker_id,
                first_motion_correction_id,
                auto_proc_program_id,
                particle_picking_template,
                particle_diameter,
                number_of_particles,
                summary_image_full_path,
            ),
        )

    def insert_particle_classification_group(
        self,
        particle_classification_group_id=None,
        particle_picker_id=None,
        auto_proc_program_id=None,
        type=None,
        batch_number=None,
        number_of_particles_per_batch=None,
        number_of_classes_per_batch=None,
        symmetry=None,
    ):
        """Store new particle classification group parameters."""
        return self.get_connection().call_sp_write(
            procname="upsert_particle_classification_group",
            args=(
                particle_classification_group_id,
                particle_picker_id,
                auto_proc_program_id,
                type,
                batch_number,
                number_of_particles_per_batch,
                number_of_classes_per_batch,
                symmetry,
            ),
        )

    def insert_particle_classification(
        self,
        particle_classification_id=None,
        particle_classification_group_id=None,
        class_number=None,
        class_image_full_path=None,
        particles_per_class=None,
        class_distribution=None,
        rotation_accuracy=None,
        translation_accuracy=None,
        estimated_resolution=None,
        overall_fourier_completeness=None,
    ):
        """Store new particle classification parameters."""
        return self.get_connection().call_sp_write(
            procname="upsert_particle_classification_v2",
            args=(
                particle_classification_id,
                particle_classification_group_id,
                class_number,
                class_image_full_path,
                particles_per_class,
                class_distribution,
                rotation_accuracy,
                translation_accuracy,
                estimated_resolution,
                overall_fourier_completeness,
            ),
        )

    def insert_cryoem_initial_model(
        self,
        cryoem_initial_model_id=None,
        particle_classification_id=None,
        resolution=None,
        number_of_particles=None,
    ):
        """Store new cryo-em initial model parameters."""
        return self.get_connection().call_sp_write(
            procname="insert_cryoem_initial_model",
            args=(
                cryoem_initial_model_id,
                particle_classification_id,
                resolution,
                number_of_particles,
            ),
        )
