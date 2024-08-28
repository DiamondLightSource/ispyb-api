#!/usr/bin/env python
#
# Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2015-06-22
#
# Usage example:
# python em_put_particle.py --movieid=1 --x=123.4 --y=50.02

import logging
import sys

if __name__ == "__main__":
    from ispyb_api.dbconnection import dbconnection
    from ispyb_api.em import em

    def exit(code, message=None):
        dbconnection.disconnect()
        if message is not None:
            print(message)
        sys.exit(code)

    logging.info("test")

    import optparse

    parser = optparse.OptionParser()
    parser.add_option(
        "--particleid", dest="particleid", help="Id for particle", metavar="INTEGER"
    )
    parser.add_option("--movieid", dest="dcid", help="Id for movie", metavar="INTEGER")
    parser.add_option("--x", dest="x", help="x coordinate", metavar="FLOAT")
    parser.add_option("--y", dest="y", help="y coordinate", metavar="FLOAT")
    parser.add_option(
        "--db",
        dest="db",
        help="Database to use: dev, test or prod (default)",
        metavar="STRING",
    )

    (opts, args) = parser.parse_args()

    cursor = None
    if opts.db is None or opts.db == "prod":
        cursor = dbconnection.connect_to_prod()
    elif opts.db == "dev":
        cursor = dbconnection.connect_to_dev()
    elif opts.db == "test":
        cursor = dbconnection.connect_to_test()
    else:
        exit(1, "ERROR: Invalid database")

    if opts.particleid is None and opts.dcid is None:
        exit(1, "ERROR: Both movieid and particleid are None.")

    p_id = em.put_particle(cursor, opts.particleid, opts.dcid, opts.x, opts.y)
    exit(0, "--particleid=%d" % p_id)
