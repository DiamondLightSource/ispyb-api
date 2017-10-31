from __future__ import absolute_import, division

import ispyb.legacy.interface.datacollection
import ispyb.legacy.interface.processing
import ispyb.legacy.interface.reprocessing

class IF(ispyb.legacy.interface.datacollection.IF,
         ispyb.legacy.interface.processing.IF,
         ispyb.legacy.interface.reprocessing.IF):
  '''ISPyB interface definition object.'''

  def _notimplemented(self):
    '''Overrideable function which is called when a driver lacks an
       implementation for an interface function. In general this function
       should always end in an exception being raised.'''
    raise NotImplementedError('This call is not supported by the selected '
                              'ISPyB driver.')
