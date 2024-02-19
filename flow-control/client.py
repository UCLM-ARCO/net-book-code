#!/usr/bin/env -S python -u

import sys
import socket
import time

BLOCK = b'x' * 20*10**4

class Sender:
    def __init__(self, host, port):
        self.sock = socket.socket()
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
            self.log()
            self.sock.sendall(BLOCK)
            self.sent += len(BLOCK)

    def log (self):
        elapsed = time.time() - self.init
        msg = f'sent:{self.sent//10**3:,} kB, rate:{self.sent/10**3//elapsed:,} kB/s'

        sys.stderr.write(f'\r{"-"*40}\r'); sys.stderr.flush()
        time.sleep(0.01)
        sys.stderr.write(f'\r{" "*40}\r' + msg); sys.stderr.flush()


host, port = sys.argv[1], int(sys.argv[2])
Sender(host, port).run()
