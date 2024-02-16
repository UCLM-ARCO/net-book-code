#!/usr/bin/env -S python -u

import sys
import socket
import time

s = socket.socket()
s.bind(('', int(sys.argv[1])))
s.listen(10)

child, client = s.accept()

start = time.time()
received = 0

while 1:
    elapsed = time.time() - start
    print(f'received:{received/10**3:,.0f} kB - rate:{received/10**3/elapsed:,.0f} kB/s',
        end='', flush=True)

    time.sleep(0.1)
    data = child.recv(5*10**4)
    if not data:
        break

    received += len(data)
    print('\r' + ' ' * 40 + '\r', end='', flush=True)

s.close()