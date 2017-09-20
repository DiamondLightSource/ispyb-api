from __future__ import absolute_import, division

import ispyb.driver.mysql.stored_procedures
import mock
import pytest

def test_stored_procedure_interface_only_provides_public_names_beginning_with_sp_():
  MSPI = ispyb.driver.mysql.stored_procedures.MySQLStoredProcedureInterface()

  public_names = filter(lambda n: not n.startswith('_'), dir(MSPI))
  disallowed_names = list(filter(lambda n: not n.startswith('sp_'), public_names))

  assert not disallowed_names, \
       "Found public names not starting with 'sp_':\n" + \
       "\n".join(sorted(disallowed_names))
