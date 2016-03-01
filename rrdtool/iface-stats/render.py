#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import rrdtool

ret = rrdtool.graph(
    "net.png",
    "--start", "-30min",
    "--vertical-label=bytes/s",
    "DEF:inoctets=net.rrd:downstream:AVERAGE",
    "DEF:outoctets=net.rrd:upstream:AVERAGE",
    "AREA:inoctets#00FF00:Downstream",
    "LINE1:outoctets#0000FF:Upstream",
    "CDEF:inbits=inoctets,8,*",
    "CDEF:outbits=outoctets,8,*",
    "COMMENT:\\n",
    "GPRINT:inbits:AVERAGE:Avg downstream\: %6.2lf %Sbps",
    "COMMENT:  ",
    "GPRINT:inbits:MAX:Max downstream\: %6.2lf %Sbps\\r",
    "GPRINT:outbits:AVERAGE:Avg upstream\: %6.2lf %Sbps",
    "COMMENT: ",
    "GPRINT:outbits:MAX:Max upstream\: %6.2lf %Sbps\\r")
