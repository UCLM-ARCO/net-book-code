#!/usr/bin/env -S python -u

import sys
import socket
import time


class Receiver:
    def __init__(self, port):
        self.sock = socket.socket()
        self.sock.setsockopt(
            socket.SOL_SOCKET, socket.SO_RCVBUF, 2048)

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

            self.log()
            self.received += len(data)

            sys.stdout.buffer.write(data)
            sys.stdout.buffer.flush()

    def log(self):
        elapsed = time.time() - self.init
        msg = f'received:{self.received//1000:,} kB, rate:{(self.received*8)/1000//elapsed:,} kbps'
        sys.stderr.write(f'\r{" "*40}\r' + msg)
        sys.stderr.flush()


port = int(sys.argv[1])
Receiver(port).run()
