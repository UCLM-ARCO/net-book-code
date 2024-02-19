#!/usr/bin/env -S python -u

import sys
import socket
import time


class Receiver:
    def __init__(self, port):
        self.sock = socket.socket()
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
            # input('>')

            time.sleep(0.1)
            data = self.child.recv(5*10**4)
            if not data:
                break

            self.log()
            self.received += len(data)


    def log(self):
        elapsed = time.time() - self.init
        msg = f'received:{self.received/10**3:,} kB, rate:{self.received/10**3//elapsed:,} kB/s'
        sys.stderr.write(f'\r{" "*40}\r' + msg)
        sys.stderr.flush()


port = int(sys.argv[1])
Receiver(port).run()
