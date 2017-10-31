from __future__ import absolute_import, division

# Context handlers for database cursors,
# ensuring that cursors are closed after use.

class contextcursor_factory(object):
  '''This class creates basic context manager objects for mysql.connector
     cursors. By using a context manager it is ensured that cursors are
     closed immediately after use.'''

  @staticmethod
  def default_cursor_options():
    '''Overridable extension method to set default cursor constructor
       keyword arguments.'''
    return {}

  @staticmethod
  def add_specific_calls(cursor):
    '''Overridable extension method to modify the cursor object before it is
       passed to the code inside the context.'''
    return

  def __init__(self, cursor_factory_function):
    '''Set up the context manager factory.'''

    class contextmanager(object):
      '''The context manager object which is actually used in the
            with .. as ..:
         clause.'''

      def __init__(cm, parameters):
        '''Store any constructor parameters, given as dictionary, so that they
           can be passed to the cursor factory later.'''
        cm.cursorparams = self.default_cursor_options()
        cm.cursorparams.update(parameters)

      def __enter__(cm):
        '''Enter context. Instantiate and return the actual cursor using the
           given constructor, parameters and extra call decorations.'''
        cm.cursor = cursor_factory_function(**cm.cursorparams)
        self.add_specific_calls(cm.cursor)
        return cm.cursor

      def __exit__(cm, *args):
        '''Leave context. Close cursor. Destroy reference.'''
        cm.cursor.close()
        cm.cursor = None

    self._contextmanager_factory = contextmanager

  def __call__(self, **parameters):
    '''Creates and returns a context manager object.'''
    return self._contextmanager_factory(parameters)

class dictionary_contextcursor_factory(contextcursor_factory):
  '''Context managers created via this factory return results as a dictionary
     by default, and offer a .run() function, which is an alias to .execute
     that accepts query parameters as function parameters rather than a list.
  '''

  @staticmethod
  def default_cursor_options():
    '''By default create dictionary cursors.'''
    return { 'dictionary': True }

  @staticmethod
  def add_specific_calls(cursor):
    '''Add a .run() function to newly instantiated cursors.'''

    def flat_execute(stmt, *parameters):
      '''Pass all given function parameters as a list to the existing
         .execute() function.'''
      return cursor.execute(stmt, parameters)

    setattr(cursor, 'run', flat_execute)

class stored_proc_contextcursor_factory(contextcursor_factory):
  '''Context managers created via this factory include a .call() function
     which can be used to run stored procedures.
  '''

  @staticmethod
  def add_specific_calls(cursor):
    '''Add a .call() function to newly instantiated cursors.'''

    def flat_call_procedure(procedure_name, arguments):
      '''At this point this is just an alias to .callproc().'''
      return cursor.callproc(procedure_name, arguments)

    setattr(cursor, 'call', flat_call_procedure)
