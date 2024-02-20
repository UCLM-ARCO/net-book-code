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
        self.sock.bind(('', port))
        self.sock.listen(1)
        self.child, client = self.sock.accept()
        self.init = time.time()
        self.received = 0
        rcv_buffer = self.child.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        log(f'receiving window size: {rcv_buffer:,} B\n')

    def run(self):
        try:
            self.receiving()
        except KeyboardInterrupt:
            self.sock.close()

    def receiving(self):
        while 1:
            # input('>')

            time.sleep(0.1)
            data = self.child.recv(5*10**4)
            if not data:
                break

            self.stats()
            self.received += len(data)


    def stats(self):
        elapsed = time.time() - self.init
        msg = f'received:{self.received/1000:,} kB, '
        msg += f'rate:{self.received/1000//elapsed:,.0f} kB/s'
        log(f'\r{" "*40}\r' + msg)


port = int(sys.argv[1])
Receiver(port).run()
