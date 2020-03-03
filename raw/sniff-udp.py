#!/usr/bin/python3
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                     socket.getprotobyname('udp'))
while 1:
    print("--\n{!r}".format(sock.recv(1600)))
