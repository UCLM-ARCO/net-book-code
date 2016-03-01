#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import rrdtool

rrdtool.graph(
    "random.png",
    "--start", "-5min",
    "DEF:random=random.rrd:value:AVERAGE",
    "AREA:random#77DD77:Random value")
