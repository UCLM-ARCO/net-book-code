#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import time
import random
import rrdtool


# http://coreygoldberg.blogspot.com.es/2010/09/python-linux-parse-network-stats-from.html
def get_network_bytes(iface):
    for line in open('/proc/net/dev', 'r'):
        if iface in line:
            data = line.split('%s:' % iface)[1].split()
            rx_bytes, tx_bytes = (data[0], data[8])
            return (int(rx_bytes), int(tx_bytes))


total_downstream = 0
total_upstream = 0

while 1:
    total_downstream, total_upstream = get_network_bytes('eth0')

    ret = rrdtool.update(
        'net.rrd', 'N:%s:%s' % (total_downstream, total_upstream))

    if ret:
        print rrdtool.error()

    time.sleep(1)
