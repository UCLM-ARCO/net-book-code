#!/usr/bin/env -S python -u

import sys
import socket
import time


def log(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()

class Receiver:
    def __init__(self, port):
        self.sock = socket.socket()
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
        log(f'receiving window size: \
            {self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)}\n')

        self.sock.bind(('', port))
        self.sock.listen(1)
        self.child, client = self.sock.accept()
        self.init = time.time()
        self.received = 0

    def run(self):
        try:
            self.receiving()
        except KeyboardInterrupt:
            self.sock.close()

    def receiving(self):
        while 1:
            data = self.child.recv(1024)
            if not data:
                break

            self.stats()
            self.received += len(data)

            sys.stdout.buffer.write(data)
            sys.stdout.buffer.flush()

    def stats(self):
        elapsed = time.time() - self.init
        msg = f'received:{self.received//1000:,} kB, '
        msg += f'rate:{(self.received*8)/1000//elapsed:,.0f} kbps'
        log(f'\r{" "*40}\r' + msg)


port = int(sys.argv[1])
Receiver(port).run()
