from __future__ import division, absolute_import

import ispyb.api.datacollection
import ispyb.api.reprocessing

class API(ispyb.api.datacollection.API,
          ispyb.api.reprocessing.API):

  def _notimplemented(self):
    '''Overrideable function which is called when a driver lacks an
       implementation for an API function. In general this function
       should always end in an exception being raised.'''
    raise NotImplementedError('This call is not supported by the selected '
                              'ISPyB driver.')
