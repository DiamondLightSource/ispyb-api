import argparse
import logging

from ispyb.simulation.datacollection import SimulateDataCollection

try:
    import zocalo
    import zocalo.configuration
except ModuleNotFoundError:
    zocalo = None

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def run():
    try:
        sdc = SimulateDataCollection()
    except AttributeError as e:
        exit(f"Simulation Error: {e}")

    parser = argparse.ArgumentParser(description="ISPyB simulation tool")
    parser.add_argument(
        "beamline",
        help=f"Beamline to run simulation against",
        choices=sdc.beamlines
    )

    parser.add_argument(
        "experiment",
        help=f"Experiment to simluate",
        choices=sdc.experiments
    )

    parser.add_argument(
        "--delay",
        default=5,
        type=int,
        dest="delay",
        help="Delay between mimas start and end events",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output",
    )

    if zocalo:
        zc = zocalo.configuration.from_file()
        zc.activate()
        zc.add_command_line_options(parser)

    args = parser.parse_args()

    root = logging.getLogger()
    root.setLevel(level=logging.DEBUG if args.debug else logging.INFO)

    try:
        sdc.do_run(
            args.beamline, args.experiment, delay=args.delay
        )
    except Exception as e:
        if args.debug:
            logger.exception("Simulation Error")
            print(e)
        else:
            print(f"Simulation Error: {str(e)}")
