#!/usr/bin/python3
# -*- coding:utf-8; tab-width:4; mode:python -*-

import socket
QUIT = b"bye"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('', 12345)

while 1:
    message_out = input().encode()
    sock.sendto(message_out, server)

    if message_out == QUIT:
        break

    message_in, peer = sock.recvfrom(1024)
    print(message_in.decode())

    if message_in == QUIT:
        break
