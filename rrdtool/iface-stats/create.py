#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import rrdtool

ret = rrdtool.create(
    "net.rrd",
    "--step", "5",
    "--start", "0",
    "DS:downstream:COUNTER:50:U:U",
    "DS:upstream:COUNTER:50:U:U",
    "RRA:AVERAGE:0.5:1:600",
    "RRA:MAX:0.5:1:600")

if ret:
    print rrdtool.error()
