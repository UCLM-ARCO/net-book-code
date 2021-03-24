#!/usr/bin/python3

import socket

ETH_P_ALL = 3

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,
                     socket.htons(ETH_P_ALL))

while 1:
    print("--\n{!r}".format(sock.recvfrom(1600)))
