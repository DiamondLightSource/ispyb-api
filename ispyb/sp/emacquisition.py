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
        self.insert_data_collection_group = super(
            EMAcquisition, self
        ).upsert_data_collection_group
        self.insert_data_collection = super(EMAcquisition, self).upsert_data_collection
        self.update_data_collection_group = super(
            EMAcquisition, self
        ).upsert_data_collection_group
        self.update_data_collection = super(EMAcquisition, self).upsert_data_collection

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

    _ctf_params = StrictOrderedDict(
        [
            ("ctfId", None),
            ("motionCorrectionId", None),
            ("autoProcProgramId", None),
            ("boxSizeX", None),
            ("boxSizeY", None),
            ("minResolution", None),
            ("maxResolution", None),
            ("minDefocus", None),
            ("maxDefocus", None),
            ("defocusStepSize", None),
            ("astigmatism", None),
            ("astigmatismAngle", None),
            ("estimatedResolution", None),
            ("estimatedDefocus", None),
            ("amplitudeContrast", None),
            ("ccValue", None),
            ("fftTheoreticalFullPath", None),
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
    def get_ctf_params(cls):
        return copy.deepcopy(cls._ctf_params)

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

    def insert_ctf(self, values):
        """Store new ctf params."""
        return self.get_connection().call_sp_write(procname="upsert_ctf", args=values)

    def insert_motion_correction_drift(self, values):
        """Store new motion correction drift params."""
        return self.get_connection().call_sp_write(
            procname="upsert_motion_correction_drift", args=values
        )
