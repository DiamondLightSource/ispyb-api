#!/usr/bin/env python
#
# Copyright (C) 2014 Diamond Light Source, Karl Levik
#
# 2015-07-01
#
# Usage example:
# python put_program.py --....

import logging
import optparse
import sys

# AutoProcProgram.processingStatus:
# no row = didn't run
# NULL (None) = running
# 0 = failed
# 1 = success

if __name__ == "__main__":

    from datetime import datetime

    from ispyb_api.dbconnection import dbconnection
    from ispyb_api.mxdatareduction import mxdatareduction

    def exit(code, message=None):
        dbconnection.disconnect()
        if message is not None:
            print(message)
        sys.exit(code)

    logging.info("test")

    parser = optparse.OptionParser()
    parser.add_option("--id", dest="id", help="Id for program run", metavar="INTEGER")
    parser.add_option(
        "--cmd_line", dest="cmd_line", help="Command line", metavar="STRING"
    )
    parser.add_option(
        "--programs", dest="programs", help="Programs used", metavar="STRING"
    )
    parser.add_option(
        "--status", dest="status", help="Current processing status", metavar="STRING"
    )
    parser.add_option(
        "--message", dest="message", help="Processing message", metavar="STRING"
    )
    parser.add_option(
        "--stime",
        dest="stime",
        help="Start time (yyyy-mm-dd hh24:mi:ss)",
        metavar="TIME",
    )
    parser.add_option(
        "--etime", dest="etime", help="End time (yyyy-mm-dd hh24:mi:ss)", metavar="TIME"
    )
    parser.add_option(
        "--envir", dest="envir", help="Processing environment", metavar="STRING"
    )
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

    # Create / update a program entry:
    params = mxdatareduction.get_program_params()
    if opts.id is not None:
        params["id"] = int(opts.id)
    params["cmd_line"] = opts.cmd_line
    params["programs"] = opts.programs
    params["status"] = opts.status
    params["message"] = opts.message
    if opts.stime is not None:
        params["starttime"] = datetime.strptime(opts.stime, "%Y-%m-%d %H:%M:%S")
    if opts.etime is not None:
        params["endtime"] = datetime.strptime(opts.etime, "%Y-%m-%d %H:%M:%S")
    params["environment"] = opts.envir
    #    params['filename1'] = ''
    #    params['filepath1'] = ''
    #    params['filetype1'] = ''
    #    params['filename2'] = ''
    #    params['filepath2'] = ''
    #    params['filetype2'] = ''
    #    params['filename3'] = ''
    #    params['filepath3'] = ''
    #    params['filetype3'] = ''

    p_id = mxdatareduction.put_program(cursor, params.values())

    if p_id is None:
        exit(1, "ERROR: p_id is None.")  # exit code 1 - indicates error
    exit(0, "--p_id=%d" % p_id)
