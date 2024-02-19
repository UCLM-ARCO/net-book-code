#!/usr/bin/env -S python -u

import sys
import socket
import time

class Sender:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.setsockopt(
            socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)

        self.sock.connect((host, port))
        self.init = time.time()
        self.sent = 0

    def run(self):
        try:
            self.sending()
        except KeyboardInterrupt:
            self.sock.close()

    def sending(self):
        while 1:
            data = sys.stdin.buffer.read(1024)
            self.log()
            self.sock.sendall(data)
            self.sent += len(data)

    def log (self):
        elapsed = time.time() - self.init
        msg = f'sent:{self.sent//1000:,} kB, rate:{(self.sent*8)/1000//elapsed:,} kbps'
        sys.stderr.write(f'\r{" "*40}\r' + msg); sys.stderr.flush()


host, port = sys.argv[1], int(sys.argv[2])
Sender(host, port).run()
