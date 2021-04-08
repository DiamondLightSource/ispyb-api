import ispyb.model.__future__
import ispyb.model.datacollection
import ispyb.model.screening


def test_model_screening(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    dc = ispyb.model.datacollection.DataCollection(1052494, testdb)
    assert len(dc.screenings) == 7

    for screening in (
        dc.screenings[2],
        ispyb.model.screening.Screening(dc.screenings[2].screening_id, testdb),
    ):
        assert screening.program == "EDNA MXv1"
        assert (
            screening.comment
            == "Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s"
        )
        assert screening.short_comment == "EDNAStrategy1"
        assert len(screening.outputs) == 1

    screening_output = screening.outputs[0]
    assert len(screening_output.lattices) == 1
    assert len(screening_output.strategies) == 1

    for sol in (
        screening_output.lattices[0],
        ispyb.model.screening.ScreeningOutputLattice(
            screening_output.lattices[0].lattice_id, testdb
        ),
    ):
        assert sol.unit_cell.a == 76.3
        assert sol.unit_cell.b == 76.3
        assert sol.unit_cell.c == 76.3
        assert sol.unit_cell.alpha == 90.0
        assert sol.unit_cell.beta == 90.0
        assert sol.unit_cell.gamma == 90.0
        assert sol.spacegroup == "I23"

    for strategy in (
        screening_output.strategies[0],
        ispyb.model.screening.ScreeningStrategy(
            screening_output.strategies[0].strategy_id, testdb
        ),
    ):
        assert strategy.anomalous == 0
        assert strategy.exposure_time == 0.428
        assert strategy.program == "BEST"
        assert strategy.ranking_resolution == 1.41
        assert len(strategy.wedges) == 1

    for wedge in (
        strategy.wedges[0],
        ispyb.model.screening.ScreeningStrategyWedge(
            strategy.wedges[0].wedge_id, testdb
        ),
    ):
        assert wedge.completeness == 1.0
        assert wedge.multiplicity == 4.07
        assert wedge.number_of_images == 220
        assert wedge.wedge_number == 1
        assert wedge.resolution == 1.41
        assert wedge.chi is None
        assert wedge.phi is None
        assert wedge.kappa is None

    assert len(wedge.sub_wedges) == 1
    for sub_wedge in (
        wedge.sub_wedges[0],
        ispyb.model.screening.ScreeningStrategySubWedge(
            wedge.sub_wedges[0].sub_wedge_id, testdb
        ),
    ):
        assert sub_wedge.axis_start == 7.0
        assert sub_wedge.axis_end == 40.0
        assert sub_wedge.completeness == 1.0
        assert sub_wedge.exposure_time == 0.428
        assert sub_wedge.multiplicity == 4.07
        assert sub_wedge.number_of_images == 220
        assert sub_wedge.oscillation_range == 0.15
        assert sub_wedge.resolution == 1.41
        assert sub_wedge.sub_wedge_number == 1
        assert sub_wedge.transmission == 100.0


def test_model_screening_str(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    screening = testdb.get_screening(1894774)
    screening.load()
    assert (
        str(screening)
        == """\
Screening #1894774
  comment         : Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s
  short_comment   : EDNAStrategy1
  program         : EDNA MXv1"""
    )


def test_model_screening_output_str(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    screening_output = testdb.get_screening_output(1489405)
    screening_output.load()
    assert (
        str(screening_output)
        == """\
ScreeningOutput #1489405
  alignment_success  : 0
  indexing_success   : 0
  strategy_success   : 0
  program            : None"""
    )


def test_model_screening_output_lattice_str(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    screening_output_lattice = testdb.get_screening_output_lattice(1309570)
    screening_output_lattice.load()
    assert (
        str(screening_output_lattice)
        == """\
ScreeningOutputLattice #1309570
  spacegroup  : I23
  a         : 76.3
  b         : 76.3
  c         : 76.3
  alpha     : 90.0
  beta      : 90.0
  gamma     : 90.0"""
    )


def test_model_screening_strategy_str(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    screening_strategy = testdb.get_screening_strategy(1473913)
    screening_strategy.load()
    assert (
        str(screening_strategy)
        == """\
ScreeningStrategy #1473913
  anomalous           : 0
  exposure_time       : 0.428
  program             : BEST
  ranking_resolution  : 1.41"""
    )


def test_model_screening_strategy_wedge_str(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    screening_strategy_wedge = testdb.get_screening_strategy_wedge(1143796)
    screening_strategy_wedge.load()
    assert (
        str(screening_strategy_wedge)
        == """\
ScreeningStrategyWedge #1143796
  chi               : None
  kappa             : None
  phi               : None
  completeness      : 1.0
  multiplicity      : 4.07
  number_of_images  : 220
  resolution        : 1.41
  wedge_number      : 1"""
    )


def test_model_screening_strategy_sub_wedge_str(testdb, testconfig):
    ispyb.model.__future__.enable(testconfig)
    screening_strategy_sub_wedge = testdb.get_screening_strategy_sub_wedge(1111570)
    screening_strategy_sub_wedge.load()
    assert (
        str(screening_strategy_sub_wedge)
        == """\
ScreeningStrategySubWedge #1111570
  axis_end           : 40.0
  axis_start         : 7.0
  completeness       : 1.0
  exposure_time      : 0.428
  multiplicity       : 4.07
  number_of_images   : 220
  oscillation_range  : 0.15
  resolution         : 1.41
  rotation_axis      : Omega
  transmission       : 100.0
  sub_wedge_number   : 1"""
    )
