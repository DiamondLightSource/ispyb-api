import argparse
import logging
import os
import pathlib
import sys
import time

import sqlalchemy.orm
from sqlalchemy.orm import Load

import ispyb
from ispyb.sqlalchemy import BLSession, DataCollection, GridInfo, Proposal


def _tty_line_length():
    if not sys.stdout.isatty():
        return False
    return os.get_terminal_size().columns


def print_data_collections(rows, synchweb_url=None, truncate_length=None):
    for row in reversed(rows):
        visit = f"{row.Proposal.proposalCode}{row.Proposal.proposalNumber}-{row.BLSession.visit_number}"
        bl_name = row.BLSession.beamLineName
        n_images = row.DataCollection.numberOfImages
        images = f"{n_images:4} images" if n_images else ""
        dcid = row.DataCollection.dataCollectionId
        template = (
            pathlib.Path(row.DataCollection.imageDirectory)
            / (row.DataCollection.fileTemplate or "")
            if row.DataCollection.imageDirectory
            else ""
        )
        start_time = (
            f"{row.DataCollection.startTime:%Y-%m-%d %H:%M}"
            if row.DataCollection.startTime
            else "????-??-?? ??:??"
        )
        grid_size = (
            f"{row.GridInfo.steps_x:.0f}x{row.GridInfo.steps_y:.0f}"
            if row.GridInfo
            else ""
        )
        grid = f", {grid_size:>5} grid" if grid_size else ""
        line = (
            f"{start_time} {bl_name:8} {dcid:8} {visit:<11} {images}{grid}   {template}"
        )
        if truncate_length and truncate_length < len(line):
            line = line[: truncate_length - 3] + "..."
        print(line)
        if synchweb_url:
            print(" " * 52 + f"{synchweb_url}/dc/visit/{visit}/id/{dcid}")


def get_last_data_collections_on(beamlines, db_session, limit=10, latest_dcid=None):
    query = (
        db_session.query(BLSession, DataCollection, GridInfo, Proposal)
        .options(
            Load(DataCollection).load_only(
                "dataCollectionId",
                "fileTemplate",
                "imageDirectory",
                "numberOfImages",
                "startTime",
            ),
            Load(Proposal).load_only("proposalCode", "proposalNumber"),
            Load(BLSession).load_only("beamLineName", "visit_number"),
            Load(GridInfo).load_only("steps_x", "steps_y"),
        )
        .join(
            BLSession,
            BLSession.sessionId == DataCollection.SESSIONID,
        )
        .join(
            Proposal,
            Proposal.proposalId == BLSession.proposalId,
        )
        .outerjoin(
            GridInfo,
            DataCollection.dataCollectionGroupId == GridInfo.dataCollectionGroupId,
        )
        .filter(BLSession.beamLineName.in_(beamlines))
        .filter(Proposal.proposalCode != "nt")
    )
    if latest_dcid:
        query = query.filter(DataCollection.dataCollectionId > latest_dcid).order_by(
            DataCollection.startTime.desc(),
        )
    else:
        query = query.order_by(DataCollection.startTime.desc()).limit(limit)
    return query.all()


def main(args=None):
    parser = argparse.ArgumentParser(
        usage="ispyb.last_data_collections_on [beamline]",
        description="Command line tool to view most recent data collections.",
    )

    parser.add_argument(
        "beamline", nargs="+", help="Show data collections for these beamlines"
    )
    parser.add_argument(
        "-f",
        "--follow",
        dest="follow",
        default=False,
        action="store_true",
        help="Keep showing new data collections as they appear.",
    )
    parser.add_argument(
        "-s",
        "--sleep",
        dest="sleep",
        default=60,
        type=float,
        help="Length of time (s) to sleep in conjunction with --follow mode.",
    )
    parser.add_argument(
        "-l",
        "--link",
        action="store_true",
        dest="link",
        default=False,
        help="show SynchWeb links for each data collection",
    )
    parser.add_argument(
        "-n",
        "--collections",
        action="store",
        dest="limit",
        default=20,
        type=int,
        metavar="N",
        help="show the last N collections for each beamline",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        dest="debug",
        default=False,
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--credentials", action="store", type=pathlib.Path)
    parser.add_argument(
        "--synchweb-url",
        dest="synchweb_url",
        default="https://ispyb.diamond.ac.uk",
        type=str,
        help="Base URL for SynchWeb links",
    )
    args = parser.parse_args(args)

    if not args:
        parser.print_help()
        sys.exit(0)
    t0 = time.time()

    if args.debug:
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.DEBUG)
        logging.getLogger("ispyb").addHandler(console)
        logging.getLogger("ispyb").setLevel(logging.DEBUG)
        ispyb.sqlalchemy.enable_debug_logging()

    url = ispyb.sqlalchemy.url(args.credentials)
    engine = sqlalchemy.create_engine(url, connect_args={"use_pure": True})
    Session = sqlalchemy.orm.sessionmaker(bind=engine)

    latest_dcid = None
    print("------Date------ Beamline --DCID-- ---Visit---")
    # Terminate after 24 hours
    while time.time() - t0 < 60 * 60 * 24:
        with Session() as db_session:
            rows = get_last_data_collections_on(
                args.beamline, db_session, limit=args.limit, latest_dcid=latest_dcid
            )
        if rows:
            # Record the last observed dcid per beamline
            latest_dcid = rows[0].DataCollection.dataCollectionId
            print_data_collections(
                rows,
                synchweb_url=args.synchweb_url if args.link else None,
                truncate_length=_tty_line_length(),
            )
        if not args.follow:
            break
        time.sleep(args.sleep)


if __name__ == "__main__":
    main()
