#!/usr/bin/python3
"sniff and print hex dump of all ethernet frames using wireshark style"

import time
import socket

from string import printable

NON_PRINTABLE_TO_DOTS = bytes([c if chr(c) in printable[:-5] else ord('.') for c in range(256)])


def hexdump(frame):
    def to_chr(byteseq):
        retval = byteseq.translate(NON_PRINTABLE_TO_DOTS)
        return (retval[:8] + b' ' + retval[8:]).decode()

    def to_hex(byteseq):
        retval = str.join(' ', ["%02X" % x for x in byteseq])
        return retval[:23] + ' ' + retval[23:]

    print("-- {}".format(time.strftime("%H:%M:%s")))
    for i in range(0, len(frame), 16):
        line = frame[i:i+16]
        print("{:03X}   {:<49} |{:<17}|".format(i, to_hex(line), to_chr(line)))


ETH_P_ALL = 3

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
while 1:
    hexdump(s.recv(1600))
