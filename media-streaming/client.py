#!/usr/bin/env -S python -u

import sys
import socket
import time


def log(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()

class Sender:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)

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
            self.stats()
            self.sock.sendall(data)
            self.sent += len(data)

    def stats(self):
        elapsed = time.time() - self.init
        msg = f'sent:{self.sent//1000:,} kB, '
        msg += f'rate:{(self.sent*8)/1000//elapsed:,.0f} kbps'
        log(f'\r{" "*40}\r' + msg); sys.stderr.flush()


host, port = sys.argv[1], int(sys.argv[2])
Sender(host, port).run()
