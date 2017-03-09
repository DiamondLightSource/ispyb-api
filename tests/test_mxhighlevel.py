#!/usr/bin/env python

import sys
sys.path.append('..')
from ispyb.mxhighlevel import mxhighlevel

def test_store_i19_screen():
    mxhighlevel.store_i19_screen(10010, space_groups_and_unit_cells=None, dynamic_range=None, histogram=None)
