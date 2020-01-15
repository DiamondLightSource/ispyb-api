from __future__ import absolute_import, division, print_function

from datetime import datetime


def test_insert_all_screening(testdb):
    core = testdb.core
    mxscreening = testdb.mx_screening
    mxacquisition = testdb.mx_acquisition

    test_session = "cm14451-2"
    session_id = core.retrieve_visit_id(test_session)

    assert session_id is not None
    assert session_id > 0

    params = mxacquisition.get_data_collection_group_params()
    params["parentid"] = session_id
    # experimenttype must be one of the allowed values: None, 'SAD', 'SAD - Inverse Beam', 'OSC', 'Collect - Multiwedge', 'MAD', 'Helical', 'Multi-positional', 'Mesh',  'Burn', 'MAD - Inverse Beam', 'Screening'
    params["experimenttype"] = "OSC"
    params["starttime"] = datetime.strptime("2017-03-15 13:00:00", "%Y-%m-%d %H:%M:%S")
    params["endtime"] = datetime.strptime("2017-03-15 13:00:10", "%Y-%m-%d %H:%M:%S")
    params["comments"] = "This is a test of data collection group."
    # params[''] = 'something'
    dcg_id = mxacquisition.insert_data_collection_group(list(params.values()))

    params = mxscreening.get_screening_params()
    params["dcgid"] = dcg_id
    params["program_version"] = "EDNA 1.0"
    params["short_comments"] = "ENDAStrategy1"
    params["comments"] = "param1 = 1.2, param2 = 2.06"

    s_id = mxscreening.insert_screening(list(params.values()))
    assert s_id is not None
    assert s_id > 0

    params = mxscreening.get_screening_input_params()
    params["screening_id"] = s_id
    params["beamx"] = 20.2
    params["beamy"] = 25.6
    params["rms_err_lim"] = 2.09
    params["min_fraction_indexed"] = 0.10
    params["max_fraction_rejected"] = 0.30
    params["min_signal2noise"] = 0.98

    si_id = mxscreening.insert_screening_input(list(params.values()))
    assert si_id is not None
    assert si_id > 0

    params = mxscreening.get_screening_output_params()
    params["screening_id"] = s_id
    params["status_description"] = "success"
    params["rejected_reflections"] = 16
    params["resolution_obtained"] = 2.0
    params["mosaicity"] = 20.86
    params["beam_shift_x"] = 14
    params["beam_shift_y"] = 11
    params["num_spots_found"] = 120
    params["num_spots_used"] = 104
    params["diffraction_rings"] = False
    params["indexing_success"] = True
    params["strategy_success"] = True

    so_id = mxscreening.insert_screening_output(list(params.values()))
    assert so_id is not None
    assert so_id > 0

    params = mxscreening.get_screening_output_lattice_params()
    params["screening_output_id"] = so_id
    params["spacegroup"] = "P21"
    params["pointgroup"] = "P2"
    params["bravais_lattice"] = "monoclinic"
    params["unit_cell_a"] = 11
    params["unit_cell_b"] = 11
    params["unit_cell_c"] = 11
    params["unit_cell_alpha"] = 90
    params["unit_cell_beta"] = 90
    params["unit_cell_gamma"] = 90
    params["labelit_indexing"] = True

    sol_id = mxscreening.insert_screening_output_lattice(list(params.values()))
    assert sol_id is not None
    assert sol_id > 0

    params = mxscreening.get_screening_strategy_params()
    params["screening_output_id"] = so_id
    params["anomalous"] = 1.198145

    ss_id = mxscreening.insert_screening_strategy(list(params.values()))
    assert ss_id is not None
    assert ss_id > 0

    params = mxscreening.get_screening_strategy_wedge_params()
    params["screening_strategy_id"] = ss_id

    ssw_id = mxscreening.insert_screening_strategy_wedge(list(params.values()))
    assert ssw_id is not None
    assert ssw_id > 0

    params = mxscreening.get_screening_strategy_sub_wedge_params()
    params["screening_strategy_wedge_id"] = ssw_id

    id = mxscreening.insert_screening_strategy_sub_wedge(list(params.values()))
    assert id is not None
    assert id > 0


def test_model_screening(testdb):
    import ispyb.model.__future__

    ispyb.model.__future__.enable("/dls_sw/apps/zocalo/secrets/credentials-ispyb.cfg")

    import ispyb.model.screening

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
        assert strategy.program == "BEST"
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
