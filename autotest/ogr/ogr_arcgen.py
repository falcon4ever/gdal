#!/usr/bin/env python
###############################################################################
# $Id$
#
# Project:  GDAL/OGR Test Suite
# Purpose:  Test read functionality for OGR Arc/Info generate driver.
# Author:   Even Rouault <even dot rouault at mines dash paris dot org>
#
###############################################################################
# Copyright (c) 2011, Even Rouault <even dot rouault at mines-paris dot org>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
###############################################################################

import sys


import gdaltest
import ogrtest
from osgeo import ogr

###############################################################################
# Read points


def test_ogr_arcgen_points():

    ds = ogr.Open('data/points.gen')
    assert ds is not None, 'cannot open dataset'

    assert ds.GetLayerCount() == 1, 'bad layer count'

    lyr = ds.GetLayer(0)
    assert lyr is not None, 'cannot find layer'

    assert lyr.GetGeomType() == ogr.wkbPoint, 'bad layer geometry type'

    feat = lyr.GetNextFeature()
    if feat.GetField(0) != 1:
        gdaltest.post_reason('did not get expected ID')
        feat.DumpReadable()
        return 'fail'
    if ogrtest.check_feature_geometry(feat, 'POINT (2 49)',
                                      max_error=0.0000001) != 0:
        gdaltest.post_reason('did not get expected first geom')
        feat.DumpReadable()
        return 'fail'

    return 'success'

###############################################################################
# Read points25d


def test_ogr_arcgen_points25d():

    ds = ogr.Open('data/points25d.gen')
    assert ds is not None, 'cannot open dataset'

    assert ds.GetLayerCount() == 1, 'bad layer count'

    lyr = ds.GetLayer(0)
    assert lyr is not None, 'cannot find layer'

    assert lyr.GetGeomType() == ogr.wkbPoint25D, 'bad layer geometry type'

    feat = lyr.GetNextFeature()
    if feat.GetField(0) != 1:
        gdaltest.post_reason('did not get expected ID')
        feat.DumpReadable()
        return 'fail'
    if ogrtest.check_feature_geometry(feat, 'POINT (2 49 10)',
                                      max_error=0.0000001) != 0:
        gdaltest.post_reason('did not get expected first geom')
        feat.DumpReadable()
        return 'fail'

    return 'success'

###############################################################################
# Read lines


def test_ogr_arcgen_lines():

    ds = ogr.Open('data/lines.gen')
    assert ds is not None, 'cannot open dataset'

    lyr = ds.GetLayer(0)
    assert lyr is not None, 'cannot find layer'

    assert lyr.GetGeomType() == ogr.wkbLineString, 'bad layer geometry type'

    feat = lyr.GetNextFeature()
    if feat.GetField(0) != 1:
        gdaltest.post_reason('did not get expected ID')
        feat.DumpReadable()
        return 'fail'
    if ogrtest.check_feature_geometry(feat, 'LINESTRING (2 49,3 50)',
                                      max_error=0.0000001) != 0:
        gdaltest.post_reason('did not get expected first geom')
        feat.DumpReadable()
        return 'fail'

    return 'success'

###############################################################################
# Read lines25d


def test_ogr_arcgen_lines25d():

    ds = ogr.Open('data/lines25d.gen')
    assert ds is not None, 'cannot open dataset'

    lyr = ds.GetLayer(0)
    assert lyr is not None, 'cannot find layer'

    assert lyr.GetGeomType() == ogr.wkbLineString25D, 'bad layer geometry type'

    feat = lyr.GetNextFeature()
    if feat.GetField(0) != 1:
        gdaltest.post_reason('did not get expected ID')
        feat.DumpReadable()
        return 'fail'
    if ogrtest.check_feature_geometry(feat, 'LINESTRING (2 49 10,3 50 10)',
                                      max_error=0.0000001) != 0:
        gdaltest.post_reason('did not get expected first geom')
        feat.DumpReadable()
        return 'fail'

    return 'success'

###############################################################################
# Read polygons


def test_ogr_arcgen_polygons():

    ds = ogr.Open('data/polygons.gen')
    assert ds is not None, 'cannot open dataset'

    lyr = ds.GetLayer(0)
    assert lyr is not None, 'cannot find layer'

    assert lyr.GetGeomType() == ogr.wkbPolygon, 'bad layer geometry type'

    feat = lyr.GetNextFeature()
    if feat.GetField(0) != 1:
        print('did not get expected ID')
        feat.DumpReadable()
        return 'fail'
    if ogrtest.check_feature_geometry(feat, 'POLYGON ((2 49,2 50,3 50,3 49,2 49))',
                                      max_error=0.0000001) != 0:
        gdaltest.post_reason('did not get expected first geom')
        feat.DumpReadable()
        return 'fail'

    return 'success'

###############################################################################
# Read polygons25d


def test_ogr_arcgen_polygons25d():

    ds = ogr.Open('data/polygons25d.gen')
    assert ds is not None, 'cannot open dataset'

    lyr = ds.GetLayer(0)
    assert lyr is not None, 'cannot find layer'

    assert lyr.GetGeomType() == ogr.wkbPolygon25D, 'bad layer geometry type'

    feat = lyr.GetNextFeature()
    if feat.GetField(0) != 1:
        gdaltest.post_reason('did not get expected ID')
        feat.DumpReadable()
        return 'fail'
    if ogrtest.check_feature_geometry(feat, 'POLYGON ((2 49 10,2 50 10,3 50 10,3 49 10,2 49 10))',
                                      max_error=0.0000001) != 0:
        gdaltest.post_reason('did not get expected first geom')
        feat.DumpReadable()
        return 'fail'

    return 'success'


gdaltest_list = [
    test_ogr_arcgen_points,
    test_ogr_arcgen_points25d,
    test_ogr_arcgen_lines,
    test_ogr_arcgen_lines25d,
    test_ogr_arcgen_polygons,
    test_ogr_arcgen_polygons25d]


if __name__ == '__main__':

    gdaltest.setup_run('ogr_arcgen')

    gdaltest.run_tests(gdaltest_list)

    sys.exit(gdaltest.summarize())
