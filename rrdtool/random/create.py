#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import rrdtool

ret = rrdtool.create(
    "random.rrd",
    "--step", "2",
    "--start", "0",
    "DS:value:COUNTER:600:U:U",
    "RRA:AVERAGE:0.5:1:600")

if ret:
    print rrdtool.error()
