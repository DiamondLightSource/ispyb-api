=====
Usage
=====

To use the ISPyB API in a project::

    import ispyb
    i = ispyb.open('/path/to/a/configuration/file')

Command line tools
==================


``ispyb.last_collections_on``
-----------------------------

A command line tool to view most recent data collections::

    $ ispyb.last_collections_on i03
    ------Date------ Beamline --DCID-- ---Visit---
    2021-01-01 12:04 i03       1234567 ab12345-67    80 images,  1x80 grid   /dls/i03/data/2021/ab12345-67/xraycentring/auto/test_master.h5
    2021-01-01 12:05 i03       2345678 ab12345-67  3600 images   /dls/i03/data/2021/ab12345-67/auto/test_master.h5


``ispyb.job``
-------------

A command line tool to view, create, and update processing jobs.

Create a new processing job::
    ispyb.job --new --display "Dataprocessor 2000" --comment "The best program in the universe" \
              --recipe dp2000 --add-param "spacegroup:P 21 21 21" --add-sweep 1234:1:600

Display stored information::
    ispyb.job 73
    ispyb.job 73 -v  # show full record

Create new processing program row::
    ispyb.job 73 -c -p "program" -s "starting up..."

Update stored information::
    ispyb.job 73 -u 1234 -s "running..."
    ispyb.job 73 -u 1234 -s "things are happening" --update-time "2017-08-25"
    ispyb.job 73 -u 1234 -s "completed successfully" -r success
    ispyb.job 73 -u 1234 -s "everything is broken" -r failure
