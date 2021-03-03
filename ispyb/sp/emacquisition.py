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

    _motion_correction_params = StrictOrderedDict(
        [
            ("motionCorrectionId", None),
            ("movieId", None),
            ("autoProcProgramId", None),
            ("imageNumber", None),
            ("firstFrame", None),
            ("lastFrame", None),
            ("dosePerFrame", None),
            ("totalMotion", None),
            ("averageMotionPerFrame", None),
            ("driftPlotFullPath", None),
            ("micrographFullPath", None),
            ("micrographSnapshotFullPath", None),
            ("fftFullPath", None),
            ("fftCorrectedFullPath", None),
            ("patchesUsedX", None),
            ("patchesUsedY", None),
            ("comments", None),
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
    def get_motion_correction_params(cls):
        return copy.deepcopy(cls._motion_correction_params)

    @classmethod
    def get_motion_correction_drift_params(cls):
        return copy.deepcopy(cls._motion_correction_drift_params)

    def insert_movie(self, values):
        """Store new movie params."""
        return self.get_connection().call_sp_write(procname="upsert_movie", args=values)

    def insert_motion_correction(self, values):
        """Store new motion correction params."""
        return self.get_connection().call_sp_write(
            procname="upsert_motion_correction", args=values
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
