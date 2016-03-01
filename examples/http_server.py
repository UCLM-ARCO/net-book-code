#!/usr/bin/env python3
# -*- mode:python; coding:utf-8; tab-width:4 -*-

from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
print("Open http://{}:{}".format(*server.socket.getsockname()))
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
