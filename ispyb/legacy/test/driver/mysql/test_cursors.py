from __future__ import absolute_import, division

import ispyb.legacy.driver.mysql.cursors as cursors
import mock
import pytest

class pseudo_cursor():
  def execute(self, *args, **kwargs):
    pass
  def callproc(self, *args, **kwargs):
    pass
  def close(self):
    pass

def test_basic_contextmanager_class():
  mock_cursor_factory = mock.create_autospec(pseudo_cursor)

  ctxmgr = cursors.contextcursor_factory(mock_cursor_factory)

  # Creating the context manager does not instantiate a cursor.
  mock_cursor_factory.assert_not_called()
  assert mock_cursor_factory.method_calls == []

  # Test context manager without keyword arguments
  mock_cursor_factory.reset_mock()
  with ctxmgr() as c:
    c.execute(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2)

  mock_cursor_factory.assert_called_once_with()
  assert mock_cursor_factory.method_calls == [
      mock.call().execute(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2),
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))

  # Test context manager with keyword argument
  mock_cursor_factory.reset_mock()
  with ctxmgr(keyword=mock.sentinel.cursor_kwparam) as c:
    c.execute(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2)

  mock_cursor_factory.assert_called_once_with(keyword=mock.sentinel.cursor_kwparam)
  assert mock_cursor_factory.method_calls == [
      mock.call().execute(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2),
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))

  # Test context manager property, ie. close() is always called
  mock_cursor_factory.reset_mock()
  with pytest.raises(RuntimeError):
    with ctxmgr() as c:
      raise RuntimeError

  mock_cursor_factory.assert_called_once_with()
  assert mock_cursor_factory.method_calls == [
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))


def test_dictionary_contextmanager_class():
  mock_cursor_factory = mock.create_autospec(pseudo_cursor)

  ctxmgr = cursors.dictionary_contextcursor_factory(mock_cursor_factory)

  # Creating the context manager does not instantiate a cursor.
  mock_cursor_factory.assert_not_called()
  assert mock_cursor_factory.method_calls == []

  # Test context manager without keyword arguments
  mock_cursor_factory.reset_mock()
  with ctxmgr() as c:
    c.execute(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2)

  mock_cursor_factory.assert_called_once_with(dictionary=True)
  assert mock_cursor_factory.method_calls == [
      mock.call().execute(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2),
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))

  # Test context manager with keyword argument and run method
  mock_cursor_factory.reset_mock()
  with ctxmgr(keyword=mock.sentinel.cursor_kwparam) as c:
    c.run(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2)

  mock_cursor_factory.assert_called_once_with(dictionary=True, keyword=mock.sentinel.cursor_kwparam)
  assert mock_cursor_factory.method_calls == [
      mock.call().execute(mock.sentinel.method, (mock.sentinel.param1, mock.sentinel.param2)),
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))

  # Test context manager with overridden keyword argument and run method
  mock_cursor_factory.reset_mock()
  with ctxmgr(dictionary=False) as c:
    c.run(mock.sentinel.method1, mock.sentinel.param1)
    c.run(mock.sentinel.method2)

  mock_cursor_factory.assert_called_once_with(dictionary=False)
  assert mock_cursor_factory.method_calls == [
      mock.call().execute(mock.sentinel.method1, (mock.sentinel.param1,)),
      mock.call().execute(mock.sentinel.method2, ()),
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))

  # Test context manager property, ie. close() is always called
  mock_cursor_factory.reset_mock()
  with pytest.raises(RuntimeError):
    with ctxmgr() as c:
      raise RuntimeError

  mock_cursor_factory.assert_called_once_with(dictionary=True)
  assert mock_cursor_factory.method_calls == [
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))


def test_stored_procedure_contextmanager_class():
  mock_cursor_factory = mock.create_autospec(pseudo_cursor)

  ctxmgr = cursors.stored_proc_contextcursor_factory(mock_cursor_factory)

  # Creating the context manager does not instantiate a cursor.
  mock_cursor_factory.assert_not_called()
  assert mock_cursor_factory.method_calls == []

  # Test context manager without keyword arguments
  mock_cursor_factory.reset_mock()
  with ctxmgr() as c:
    c.execute(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2)

  mock_cursor_factory.assert_called_once_with()
  assert mock_cursor_factory.method_calls == [
      mock.call().execute(mock.sentinel.method, mock.sentinel.param1, mock.sentinel.param2),
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))

  # Test context manager with keyword argument and call method
  mock_cursor_factory.reset_mock()
  with ctxmgr(keyword=mock.sentinel.cursor_kwparam) as c:
    c.call(mock.sentinel.method, (mock.sentinel.param1, mock.sentinel.param2))

  mock_cursor_factory.assert_called_once_with(keyword=mock.sentinel.cursor_kwparam)
  assert mock_cursor_factory.method_calls == [
      mock.call().callproc(mock.sentinel.method, (mock.sentinel.param1, mock.sentinel.param2)),
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))

  # Test context manager property, ie. close() is always called
  mock_cursor_factory.reset_mock()
  with pytest.raises(RuntimeError):
    with ctxmgr() as c:
      raise RuntimeError

  mock_cursor_factory.assert_called_once_with()
  assert mock_cursor_factory.method_calls == [
      mock.call().close(),
      ], "Observed calls:\n" + "\n".join(map(str, mock_cursor_factory.method_calls))
