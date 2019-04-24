from __future__ import absolute_import, division, print_function

import warnings

import ispyb

warnings.warn(
    "ispyb.exceptions is deprecated and will be removed in the next release. Use the exceptions underneath ispyb. instead.",
    DeprecationWarning,
)

ISPyBException = ispyb.ISPyBException
ISPyBConnectionException = ispyb.ConnectionError
ISPyBNoResultException = ispyb.NoResult
ISPyBWriteFailed = ispyb.ReadWriteError
ISPyBRetrieveFailed = ispyb.ReadWriteError
ISPyBKeyProblem = KeyError
