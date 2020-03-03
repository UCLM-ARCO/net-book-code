#!/usr/bin/python3
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import socket
import struct

ETH_P_ARP = 0x0806

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
                     socket.htons(ETH_P_ARP))
sock.bind(('eth0', ETH_P_ARP))

sock.send(struct.pack('!6s6sh', 6 * b'\xFF',
                      b'\x00\x01\x02\x03\x04\x05', ETH_P_ARP))
