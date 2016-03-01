#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import time
import random

import rrdtool

value = 0
while 1:
    value += random.randrange(1000, 1500)
    status = rrdtool.update('random.rrd', 'N:%s' % value)

    if status:
        print rrdtool.error()

    time.sleep(1)
