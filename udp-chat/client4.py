#!/usr/bin/env python3
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import socket
from server4 import Chat, server

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Chat(sock, server).run()
