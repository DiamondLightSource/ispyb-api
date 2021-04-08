# Enables direct database functions in places where stored procedures are not
# yet available. To use, run:
#
# import ispyb.model.__future__
# ispyb.model.__future__.enable('/path/to/.../database.cfg')

import configparser
import logging

import mysql.connector

_db_config = None


def disable():
    """Disable access to future features. Disconnect if connected."""

    global _db, _db_cc, _db_config

    if _db_config:
        _db.close()
        _db, _db_cc, _db_config = None, None, None


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
        disable()

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
        host=host,
        port=port,
        user=username,
        password=password,
        database=database,
        use_pure=True,
    )
    _db_config = configuration_file
    _db.autocommit = True

    class DictionaryCursorContextManager:
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
    ispyb.model.datacollection.DataCollection.screenings = _get_linked_screenings_for_dc
    ispyb.model.datacollection.DataCollection.pdb = _get_linked_pdb_for_dc
    import ispyb.model.processingprogram

    ispyb.model.processingprogram.ProcessingProgram.reload = _get_autoprocprogram

    import ispyb.model.screening

    ispyb.model.screening.Screening.outputs = _get_linked_outputs_for_screening
    ispyb.model.screening.Screening.reload = _get_screening

    ispyb.model.screening.ScreeningOutput.lattices = (
        _get_linked_lattices_for_screening_output
    )
    ispyb.model.screening.ScreeningOutput.strategies = (
        _get_linked_strategies_for_screening_output
    )
    ispyb.model.screening.ScreeningOutput.reload = _get_screening_output

    ispyb.model.screening.ScreeningOutputLattice.reload = _get_screening_output_lattice

    ispyb.model.screening.ScreeningStrategy.wedges = (
        _get_linked_wedges_for_screening_strategy
    )
    ispyb.model.screening.ScreeningStrategy.reload = _get_screening_strategy

    ispyb.model.screening.ScreeningStrategyWedge.sub_wedges = (
        _get_linked_sub_wedges_for_screening_strategy_wedge
    )
    ispyb.model.screening.ScreeningStrategyWedge.reload = _get_screening_strategy_wedge

    ispyb.model.screening.ScreeningStrategySubWedge.reload = (
        _get_screening_strategy_sub_wedge
    )

    import ispyb.model.image_quality_indicators

    ispyb.model.image_quality_indicators.ImageQualityIndicators.reload = (
        _get_image_quality_indicators
    )

    ispyb.model.image_quality_indicators.ImageQualityIndicatorsList.reload = (
        _get_image_quality_indicators_for_dcid
    )

    ispyb.model.datacollection.DataCollection.image_quality = (
        _get_linked_image_quality_indicators_for_data_collection
    )

    import ispyb.model.detector

    ispyb.model.detector.Detector.reload = _get_detector

    import ispyb.model.sample

    ispyb.model.sample.Sample.reload = _get_sample
    ispyb.model.datacollection.DataCollection.sample = _get_linked_sample_for_dcid

    import ispyb.model.samplegroup

    ispyb.model.samplegroup.SampleGroup.reload = _get_sample_group
    ispyb.model.datacollection.DataCollection.sample_groups = (
        _get_linked_sample_groups_for_dcid
    )


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


@property
def _get_linked_screenings_for_dc(self):
    import ispyb.model.screening

    with _db_cc() as cursor:
        cursor.run(
            "SELECT screeningId, comments, shortComments, programVersion "
            "FROM Screening "
            "WHERE dataCollectionId = %s "
            "ORDER BY screeningId",
            self.dcid,
        )
        return [
            ispyb.model.screening.Screening(ir["screeningId"], self._db, preload=ir)
            for ir in cursor.fetchall()
        ]


@property
def _get_linked_outputs_for_screening(self):
    import ispyb.model.screening

    with _db_cc() as cursor:
        cursor.run(
            "SELECT screeningOutputId, alignmentSuccess, indexingSuccess, strategySuccess, program "
            "FROM ScreeningOutput "
            "WHERE screeningid = %s "
            "ORDER BY screeningOutputId",
            self._screening_id,
        )
        return [
            ispyb.model.screening.ScreeningOutput(
                ir["screeningOutputId"], self._db, preload=ir
            )
            for ir in cursor.fetchall()
        ]


@property
def _get_linked_lattices_for_screening_output(self):
    import ispyb.model.screening

    with _db_cc() as cursor:
        cursor.run(
            "SELECT screeningOutputLatticeId, spaceGroup, "
            "unitCell_a, unitCell_b, unitCell_c, "
            "unitCell_alpha, unitCell_beta, unitCell_gamma "
            "FROM ScreeningOutputLattice "
            "WHERE screeningoutputid = %s "
            "ORDER BY screeningOutputLatticeId",
            self._output_id,
        )
        return [
            ispyb.model.screening.ScreeningOutputLattice(
                ir["screeningOutputLatticeId"], self._db, preload=ir
            )
            for ir in cursor.fetchall()
        ]


@property
def _get_linked_strategies_for_screening_output(self):
    import ispyb.model.screening

    with _db_cc() as cursor:
        cursor.run(
            "SELECT screeningStrategyId, anomalous, program, "
            "exposureTime, rankingResolution "
            "FROM ScreeningStrategy "
            "WHERE screeningoutputid = %s "
            "ORDER BY screeningStrategyId",
            self._output_id,
        )
        return [
            ispyb.model.screening.ScreeningStrategy(
                ir["screeningStrategyId"], self._db, preload=ir
            )
            for ir in cursor.fetchall()
        ]


@property
def _get_linked_wedges_for_screening_strategy(self):
    import ispyb.model.screening

    with _db_cc() as cursor:
        cursor.run(
            "SELECT screeningStrategyWedgeId, chi, completeness, kappa, "
            "multiplicity, numberOfImages, phi, resolution, wedgeNumber "
            "FROM ScreeningStrategyWedge "
            "WHERE screeningStrategyId = %s "
            "ORDER BY screeningStrategyWedgeId",
            self._strategy_id,
        )
        return [
            ispyb.model.screening.ScreeningStrategyWedge(
                ir["screeningStrategyWedgeId"], self._db, preload=ir
            )
            for ir in cursor.fetchall()
        ]


@property
def _get_linked_sub_wedges_for_screening_strategy_wedge(self):
    import ispyb.model.screening

    with _db_cc() as cursor:
        cursor.run(
            "SELECT axisEnd, axisStart, completeness, exposureTime, "
            "multiplicity, numberOfImages, oscillationRange, resolution, "
            "rotationAxis, subWedgeNumber, transmission, "
            "screeningStrategySubWedgeId "
            "FROM ScreeningStrategySubWedge "
            "WHERE screeningStrategyWedgeId = %s "
            "ORDER BY screeningStrategySubWedgeId",
            self._wedge_id,
        )
        return [
            ispyb.model.screening.ScreeningStrategySubWedge(
                ir["screeningStrategySubWedgeId"], self._db, preload=ir
            )
            for ir in cursor.fetchall()
        ]


@property
def _get_linked_image_quality_indicators_for_data_collection(self):
    import ispyb.model.image_quality_indicators

    with _db_cc() as cursor:
        cursor.run(
            "SELECT imageNumber, spotTotal, goodBraggCandidates, method1Res, "
            "method2Res, totalIntegratedSignal "
            "FROM ImageQualityIndicators "
            "WHERE dataCollectionId = %s",
            self._dcid,
        )
        return ispyb.model.image_quality_indicators.ImageQualityIndicatorsList(
            self._dcid, self._db, preload=cursor.fetchall()
        )


def _get_screening(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT comments, shortComments, programVersion "
            "FROM Screening "
            "WHERE screeningId = %s",
            self._screening_id,
        )
        self._data = cursor.fetchone()


def _get_screening_output(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT alignmentSuccess, indexingSuccess, strategySuccess, program "
            "FROM ScreeningOutput "
            "WHERE screeningOutputId = %s",
            self._output_id,
        )
        self._data = cursor.fetchone()


def _get_screening_output_lattice(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT spaceGroup, unitCell_a, unitCell_b, unitCell_c, "
            "unitCell_alpha, unitCell_beta, unitCell_gamma "
            "FROM ScreeningOutputLattice "
            "WHERE screeningOutputLatticeId = %s",
            self._lattice_id,
        )
        self._data = cursor.fetchone()


def _get_screening_strategy(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT anomalous, program, exposureTime, rankingResolution "
            "FROM ScreeningStrategy "
            "WHERE screeningStrategyId = %s",
            self._strategy_id,
        )
        self._data = cursor.fetchone()


def _get_screening_strategy_wedge(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT chi, completeness, kappa, multiplicity, numberOfImages, "
            "phi, resolution, wedgeNumber "
            "FROM ScreeningStrategyWedge "
            "WHERE screeningStrategyWedgeId = %s",
            self._wedge_id,
        )
        self._data = cursor.fetchone()


def _get_screening_strategy_sub_wedge(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT axisEnd, axisStart, completeness, exposureTime, "
            "multiplicity, numberOfImages, oscillationRange, resolution, "
            "rotationAxis, subWedgeNumber, transmission "
            "FROM ScreeningStrategySubWedge "
            "WHERE screeningStrategySubWedgeId = %s",
            self._sub_wedge_id,
        )
        self._data = cursor.fetchone()


def _get_image_quality_indicators(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT spotTotal, goodBraggCandidates, method1Res, method2Res, "
            "totalIntegratedSignal "
            "FROM ImageQualityIndicators "
            "WHERE dataCollectionId = %s AND imageNumber = %s",
            self._dcid,
            self._image_number,
        )
        self._data = cursor.fetchone()


def _get_image_quality_indicators_for_dcid(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT imageNumber, spotTotal, goodBraggCandidates, method1Res, "
            "method2Res, totalIntegratedSignal "
            "FROM ImageQualityIndicators "
            "WHERE dataCollectionId = %s",
            self._dcid,
        )
        self._data = cursor.fetchall()


def _get_detector(self):
    with _db_cc() as cursor:
        cursor.run(
            "SELECT detectorType, detectorManufacturer, detectorModel, "
            "detectorPixelSizeHorizontal, detectorPixelSizeVertical, "
            "detectorSerialNumber, detectorDistanceMin, detectorDistanceMax, "
            "sensorThickness, numberOfPixelsX, numberOfPixelsY "
            "FROM Detector "
            "WHERE detectorId = %s",
            self._detectorid,
        )
        self._data = cursor.fetchone()


def _get_sample(self):
    # https://jira.diamond.ac.uk/browse/SCI-9502
    with _db_cc() as cursor:
        cursor.run(
            "SELECT blSampleId, name, "
            "crystalId, containerId "
            "FROM BLSample "
            "WHERE blSampleId = %s",
            self.id,
        )
        self._data = cursor.fetchone()

        # Get the dcids associated with this sample group
        cursor.run(
            "SELECT dataCollectionId FROM DataCollection WHERE BLSAMPLEID = %s ",
            self._data["blSampleId"],
        )
        self._data["dcids"] = [row["dataCollectionId"] for row in cursor.fetchall()]


@property
def _get_linked_sample_for_dcid(self):
    # https://jira.diamond.ac.uk/browse/SCI-9503
    import ispyb.model.sample

    with _db_cc() as cursor:
        cursor.run(
            "SELECT blSampleId FROM DataCollection WHERE dataCollectionId = %s",
            self._dcid,
        )
        data = cursor.fetchone()
        if data["blSampleId"]:
            return ispyb.model.sample.Sample(data["blSampleId"], self._db)


def _get_sample_group(self):
    # https://jira.diamond.ac.uk/browse/SCI-9379
    with _db_cc() as cursor:
        cursor.run(
            "SELECT blSampleGroupId, name "
            "FROM BLSampleGroup "
            "WHERE blSampleGroupId = %s",
            self.id,
        )
        self._data = cursor.fetchone()

        # Get the samples belonging to this sample group
        cursor.run(
            "SELECT blSampleId FROM BLSampleGroup_has_BLSample "
            "WHERE blSampleGroupId = %s "
            "ORDER BY blSampleId",
            self._data["blSampleGroupId"],
        )
        self._data["sample_ids"] = [row["blSampleId"] for row in cursor.fetchall()]

        # Get the dcids associated with this sample group
        cursor.run(
            "SELECT dataCollectionId "
            "FROM DataCollection "
            "WHERE BLSAMPLEID in (%s) "
            % ",".join(str(i) for i in self._data["sample_ids"]),
        )
        self._data["dcids"] = [row["dataCollectionId"] for row in cursor.fetchall()]


@property
def _get_linked_sample_groups_for_dcid(self):
    # https://jira.diamond.ac.uk/browse/SCI-9380
    import ispyb.model.samplegroup

    with _db_cc() as cursor:
        cursor.run(
            "SELECT b.blSampleGroupId as blSampleGroupId "
            "FROM BLSampleGroup_has_BLSample b "
            "INNER JOIN DataCollection d ON b.blSampleId = d.BLSAMPLEID "
            "WHERE dataCollectionId = %s",
            self._dcid,
        )
        return [
            ispyb.model.samplegroup.SampleGroup(row["blSampleGroupId"], self._db)
            for row in cursor.fetchall()
        ]


def test_connection():
    """A test function to verify that the database connection is alive."""
    with _db_cc() as cursor:
        cursor.run("SELECT 1")
        data = cursor.fetchall()
    assert data == [{"1": 1}]
