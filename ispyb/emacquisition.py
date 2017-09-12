#!/usr/bin/env python
# emacquisition.py
#
#    Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2014-09-24
#
# Methods to store EM acquisition data
#

try:
    import mysql.connector
except ImportError, e:
    print 'MySQL API module (mysql.connector) not found'
    raise e

from ispyb.ExtendedOrderedDict import ExtendedOrderedDict
import copy
from ispyb.storedroutines import StoredRoutines

class EMAcquisition(StoredRoutines):
    '''EMAcquisition provides methods to store data in the MotionCorrection and CTF tables.'''

    def __init__(self):
        pass

    @staticmethod
    def first_item_in_cursor(cursor):
        rs = cursor.fetchone()
        if len(rs) == 0:
            return None
        elif isinstance(cursor, mysql.connector.cursor.MySQLCursorDict):
            return rs.iteritems().next()[1]
        else:
            try:
                return int(rs[0])
            except:
                return rs[0]

    _motion_correction_params = \
        ExtendedOrderedDict(
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
        ExtendedOrderedDict(
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

    def get_motion_correction_params(self):
        return copy.deepcopy(self._motion_correction_params)

    def get_ctf_params(self):
        return copy.deepcopy(self._ctf_params)

    def insert_motion_correction(self, cursor, values):
        '''Store new motion correction params.'''
        return self.call_sp(cursor, procname='ispyb.upsert_motion_correction', args=values)[0]

    def insert_ctf(self, cursor, values):
        '''Store new ctf params.'''
        return self.call_sp(cursor, procname='ispyb.upsert_ctf', args=values)[0]

emacquisition = EMAcquisition()