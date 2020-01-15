from __future__ import absolute_import, division, print_function
import ispyb.model.screening
import ispyb.model.__future__

ispyb.model.__future__.enable("/dls_sw/apps/zocalo/secrets/credentials-ispyb.cfg")


def test_model_screening(testdb):

    screening = ispyb.model.screening.Screening(1894774, testdb)
    assert screening.program_version == "EDNA MXv1"
    assert (
        screening.comments
        == "Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s"
    )
    assert screening.short_comments == "EDNAStrategy1"

    assert len(screening.screening_outputs) == 1
    screening_output = screening.screening_outputs[0]
    assert len(screening_output.lattices) == 1
    assert len(screening_output.strategies) == 1

    for sol in (
        screening_output.lattices[0],
        ispyb.model.screening.ScreeningOutputLattice(
            screening_output.lattices[0]._lattice_id, testdb
        ),
    ):
        assert sol.unit_cell.a == 76.3
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
            screening_output.strategies[0]._strategy_id, testdb
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
            strategy.wedges[0]._strategy_wedge_id, testdb
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
            wedge.sub_wedges[0]._strategy_sub_wedge_id, testdb
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
