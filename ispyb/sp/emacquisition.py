# emacquisition.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2014-09-24
#
# Methods to store EM acquisition data
#

from ispyb.strictordereddict import StrictOrderedDict
import copy
from ispyb.sp.acquisition import Acquisition
from ispyb.version import __version__

class EMAcquisition(Acquisition):
    '''EMAcquisition provides methods to store data in the MotionCorrection and CTF tables.'''

    def __init__(self):
        pass

    _motion_correction_params = \
        StrictOrderedDict(
            [
                ('motionCorrectionId', None),
                ('dataCollectionId', None),
                ('autoProcProgramId', None),
                ('imageNumber', None),
                ('firstFrame', None),
                ('lastFrame', None),
                ('dosePerFrame', None),
                ('totalMotion', None),
                ('averageMotionPerFrame', None),
                ('driftPlotFullPath', None),
                ('micrographFullPath', None),
                ('micrographSnapshotFullPath', None),
                ('fftFullPath', None),
                ('fftCorrectedFullPath', None),
                ('patchesUsedX', None),
                ('patchesUsedY', None),
                ('comments', None)
            ]
        )

    _ctf_params = \
        StrictOrderedDict(
            [
                ('ctfId', None),
                ('motionCorrectionId', None),
                ('autoProcProgramId', None),
                ('boxSizeX', None),
                ('boxSizeY', None),
                ('minResolution', None),
                ('maxResolution', None),
                ('minDefocus', None),
                ('maxDefocus', None),
                ('defocusStepSize', None),
                ('astigmatism', None),
                ('astigmatismAngle', None),
                ('estimatedResolution', None),
                ('estimatedDefocus', None),
                ('amplitudeContrast', None),
                ('ccValue', None),
                ('fftTheoreticalFullPath', None),
                ('comments', None)
            ]
        )
    @classmethod
    def get_motion_correction_params(cls):
        return copy.deepcopy(cls._motion_correction_params)

    @classmethod
    def get_ctf_params(cls):
        return copy.deepcopy(cls._ctf_params)

    @classmethod
    def insert_motion_correction(cls, conn, values):
        '''Store new motion correction params.'''
        return cls.call_sp_write(conn, procname='upsert_motion_correction', args=values)

    @classmethod
    def insert_ctf(cls, conn, values):
        '''Store new ctf params.'''
        return cls.call_sp_write(conn, procname='upsert_ctf', args=values)

emacquisition = EMAcquisition()
