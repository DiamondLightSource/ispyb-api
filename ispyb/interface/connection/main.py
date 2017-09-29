from __future__ import absolute_import, division

class IF(object):
  '''ISPyB connection interface definition object.'''

  def _notimplemented(self):
    '''Overrideable function which is called when a driver lacks an
       implementation for an interface function. In general this function
       should always end in an exception being raised.'''
    raise NotImplementedError('This call is not supported by the selected '
                              'ISPyB driver.')
