#!/usr/bin/env python3 -u
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import socket

s = socket.socket()
s.connect(('insecure.org', 80))
s.send(b"GET /\n")
print(s.recv(2048))
