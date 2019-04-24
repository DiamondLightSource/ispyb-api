from __future__ import absolute_import, division, print_function

# Enables direct database functions in places where stored procedures are not
# yet available. To use, run:
#
# import ispyb.model.__future__
# ispyb.model.__future__.enable('/path/to/.../database.cfg')

try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import logging
import mysql.connector

_db_config = None


def enable(configuration_file, section="ispyb"):
    """Enable access to features that are currently under development."""

    global _db, _db_cc, _db_config

    if _db_config:
        if _db_config == configuration_file:
            # This database connection is already set up.
            return
        logging.getLogger("ispyb").warn(
            "__future__ configuration file change requested"
        )
        _db.close()
        _db, _db_cc, _db_config = None, None, None

    logging.getLogger("ispyb").info(
        "NOTICE: This code uses __future__ functionality in the ISPyB API. "
        "This enables unsupported and potentially unstable code, which may "
        "change from version to version without warnings. Here be dragons."
    )

    cfgparser = configparser.RawConfigParser()
    if not cfgparser.read(configuration_file):
        raise RuntimeError(
            "Could not read from configuration file %s" % configuration_file
        )
    cfgsection = dict(cfgparser.items(section))
    host = cfgsection.get("host")
    port = cfgsection.get("port", 3306)
    database = cfgsection.get("database", cfgsection.get("db"))
    username = cfgsection.get("username", cfgsection.get("user"))
    password = cfgsection.get("password", cfgsection.get("pw"))

    # Open a direct MySQL connection
    _db = mysql.connector.connect(
        host=host, port=port, user=username, password=password, database=database
    )
    _db.autocommit = True
    _db_config = configuration_file

    class DictionaryCursorContextManager(object):
        """This class creates dictionary cursors for mysql.connector connections.
        By using a context manager it is ensured that cursors are closed
        immediately after use.
        Cursors created with this context manager return results as a dictionary
        and offer a .run() function, which is an alias to .execute that accepts
        query parameters as function parameters rather than a list.
        """

        def __enter__(cm):
            """Enter context. Ensure the database is alive and return a cursor
            with an extra .run() function."""
            _db.ping(reconnect=True)
            cm.cursor = _db.cursor(dictionary=True)

            def flat_execute(stmt, *parameters):
                """Pass all given function parameters as a list to the existing
                .execute() function."""
                return cm.cursor.execute(stmt, parameters)

            setattr(cm.cursor, "run", flat_execute)
            return cm.cursor

        def __exit__(cm, *args):
            """Leave context. Close cursor. Destroy reference."""
            cm.cursor.close()
            cm.cursor = None

    _db_cc = DictionaryCursorContextManager

    import ispyb.model.datacollection

    ispyb.model.datacollection.DataCollection.integrations = (
        _get_linked_autoprocintegration_for_dc
    )
    ispyb.model.datacollection.DataCollection.pdb = _get_linked_pdb_for_dc
    import ispyb.model.processingprogram

    ispyb.model.processingprogram.ProcessingProgram.reload = _get_autoprocprogram


def _get_autoprocprogram(self):
    # https://jira.diamond.ac.uk/browse/SCI-7414
    with _db_cc() as cursor:
        cursor.run(
            "SELECT processingCommandLine as commandLine, processingPrograms as programs, "
            "processingStatus as status, processingMessage as message, processingEndTime as endTime, "
            "processingStartTime as startTime, processingEnvironment as environment, "
            "processingJobId as jobId, recordTimeStamp, autoProcProgramId "
            "FROM AutoProcProgram "
            "WHERE autoProcProgramId = %s "
            "LIMIT 1;",
            self._app_id,
        )
        self._data = cursor.fetchone()


@property
def _get_linked_autoprocintegration_for_dc(self):
    # not yet requested
    import ispyb.model.integration

    with _db_cc() as cursor:
        cursor.run(
            "SELECT * " "FROM AutoProcIntegration " "WHERE dataCollectionId = %s",
            self.dcid,
        )
        return [
            ispyb.model.integration.IntegrationResult(
                ir["autoProcIntegrationId"], self._db, preload=ir
            )
            for ir in cursor.fetchall()
        ]


@property
def _get_linked_pdb_for_dc(self):
    # https://jira.diamond.ac.uk/browse/SCI-7915
    with _db_cc() as cursor:
        cursor.run(
            "SELECT pdb.name AS name, pdb.contents AS contents, pdb.code AS code "
            "FROM Protein p "
            "INNER JOIN Crystal c ON c.proteinid = p.proteinid "
            "INNER JOIN Protein_has_PDB pp ON p.proteinid = pp.proteinid "
            "INNER JOIN BLSample b ON b.crystalid = c.crystalid "
            "INNER JOIN DataCollection d ON b.blsampleid = d.blsampleid "
            "INNER JOIN PDB pdb ON pp.pdbid = pdb.pdbid "
            "WHERE d.datacollectionid = %s;",
            self._dcid,
        )
        pdb_data = cursor.fetchall()
        if not pdb_data:
            return []
        import ispyb.model.pdb

        return [
            ispyb.model.pdb.PDB(
                name=row["name"], rawfile=row["contents"], code=row["code"]
            )
            for row in pdb_data
        ]


def test_connection():
    """A test function to verify that the database connection is alive."""
    with _db_cc() as cursor:
        cursor.run("SELECT 1")
        data = cursor.fetchall()
    assert data == [{"1": 1}]
