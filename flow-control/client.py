#!/usr/bin/env -S python -u

import sys
import socket
import time

BLOCK = b'x' * 20*10**4


def log(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()

class Sender:
    def __init__(self, host, port):
        self.sock = socket.socket()
        self.sock.connect((host, port))
        self.init = time.time()
        self.sent = 0
        snd_buffer = self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        log(f'sending window size: {snd_buffer:,} B\n')

    def run(self):
        try:
            self.sending()
        except KeyboardInterrupt:
            self.sock.close()

    def sending(self):
        while 1:
            self.stats()
            self.sock.sendall(BLOCK)
            self.sent += len(BLOCK)

    def stats(self):
        elapsed = time.time() - self.init
        msg = f'sent:{self.sent//1000:,} kB, '
        msg += f'rate:{self.sent/1000//elapsed:,.0f} kB/s'

        log(f'\r{"-"*40}\r'); sys.stderr.flush()
        time.sleep(0.01)
        log(f'\r{" "*40}\r' + msg); sys.stderr.flush()


host, port = sys.argv[1], int(sys.argv[2])
Sender(host, port).run()
