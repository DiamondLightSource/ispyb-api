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


class EMAcquisition:
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
                ('micrographfullPath', None),
                ('patchesUsed', None),
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
                ('fftPlotFullPath', None),
                ('fftPlotFullPath2', None),
                ('comments', None)
            ]
        )

    def get_motion_correction_params(self):
        return copy.deepcopy(self._motion_correction_params)

    def get_ctf_params(self):
        return copy.deepcopy(self._ctf_params)

    def insert_motion_correction(self, cursor, values):
        '''Store new motion correction params.'''
        result_args = cursor.callproc(procname='ispyb.upsert_motion_correction', args=values)
        if result_args is not None and len(result_args) > 0:
            return result_args[0]
        else:
            return None

    def insert_ctf(self, cursor, values):
        '''Store new ctf params.'''
        result_args = cursor.callproc(procname='ispyb.upsert_ctf', args=values)
        if result_args is not None and len(result_args) > 0:
            return result_args[0]
        else:
            return None

emacquisition = EMAcquisition()