#!/usr/bin/env -S python -u

import sys
import socket
import time

s = socket.socket()
s.connect((sys.argv[1], int(sys.argv[2])))

start = time.time()
sent = 0

while 1:
    elapsed = time.time() - start
    print(f'sent:{sent//10**3:,} kB, rate:{sent/10**3//elapsed:,} kB/s', end='')

    sent += s.send(b'x' * 20*10**4)

    print('\r' + '-' * 40 + '\r', end='')
    time.sleep(0.01)
    print('\r' + ' ' * 40 + '\r', end='')

s.close()
