#!/usr/bin/python3
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import socket

ETH_P_ARP = 0x0806

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
                     socket.htons(ETH_P_ARP))
sock.bind(('eth0', ETH_P_ARP))

while 1:
    print("--\n{!r}".format(sock.recv(1600)))
