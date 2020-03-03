#!/usr/bin/python3
"usage: %s <local_ip> <remote_ip>"

# arping.py
#
# Copyright (C) 2007,2020 David Villa Alises
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import sys
import struct
import socket

ETH_P_ALL = 3
ETH_P_ARP = 0x0806
ARP_REQUEST = 1
ARP_REPLY = 2
BROADCAST = 6 * b'\xFF'


class DissectionError(Exception):
    pass


class IP_address(object):
    def __init__(self, address):
        if len(address) == 4:
            address = socket.inet_ntoa(address)

        self.address = address

    def binary(self):
        return socket.inet_aton(self.address)

    def ascii(self):
        return self.address

    def __repr__(self):
        return self.ascii()


class MAC_address(object):
    null_address = 6 * b'\0'

    def __init__(self, address=None):
        assert(isinstance(address, (type(None), bytes))),\
            "Address should be bytes type: {}".format(address)
        self.address = address or self.null_address

    def binary(self):
        return self.address

    def ascii(self):
        return str.join(':', ('%02X' % b for b in self.address))

    def __repr__(self):
        return self.ascii()

    def __bool__(self):
        return self.address != self.null_address

    def __eq__(self, other):
        return self.address == other.address


class Ether(object):
    def __init__(self, src, dst, proto=None, payload=None):
        self.src = MAC_address(src)
        self.dst = MAC_address(dst)
        self.proto = proto
        self.set_payload(payload)

    def set_payload(self, payload):
        self.payload = payload
        if payload:
            self.proto = payload.proto
            payload.frame = self

    def to_stream(self):
        header = struct.pack('!6s6sh',
                             self.dst.binary(), self.src.binary(), self.payload.proto)
        retval = header + self.payload.to_stream()
        return retval + (60 - len(retval)) * b'\x00'

    @classmethod
    def from_stream(cls, frame):
        try:
            fields = struct.unpack('!6s6sh', frame[:14])
            retval = Ether(*fields)
        except struct.error:
            raise DissectionError

        if retval.proto == ETH_P_ARP:
            retval.set_payload(ARP.from_stream(frame[14:]))

        return retval


class ARP(object):
    proto = ETH_P_ARP

    def __init__(self, src, dst, hw_src=None, hw_dst=None, operation=ARP_REQUEST):
        self.src = IP_address(src)
        self.dst = IP_address(dst)
        self.hw_src = MAC_address(hw_src)
        self.hw_dst = MAC_address(hw_dst)
        self.operation = operation
        self.frame = None

    def to_stream(self):
        hw_src = self.hw_src if self.hw_src else self.frame.src
        return struct.pack('!HHbbH6s4s6s4s',
                           0x1, 0x0800,
                           6, 4, self.operation,
                           hw_src.binary(),      self.src.binary(),
                           self.hw_dst.binary(), self.dst.binary())

    @classmethod
    def from_stream(cls, frame):
        operation = struct.unpack('!H', frame[6:8])[0]

        if operation not in [ARP_REQUEST, ARP_REPLY]:
            raise DissectionError

        try:
            hw_src, src, hw_dst, dst = struct.unpack('!6s4s6s4s', frame[8:28])
            return ARP(src=src, dst=dst, hw_src=hw_src, hw_dst=hw_dst,
                       operation=operation)
        except struct.error:
            raise DissectionError

    def __str__(self):
        if self.operation == ARP_REQUEST:
            return "ARP Request: Who has {0}? Tell {1}".format(self.dst, self.src)

        if self.operation == ARP_REPLY:
            return "ARP Reply:   {0} is at {1}".format(self.dst, self.hw_src)

        return "Wrong ARP message"


def main(src_ip, dst_ip, iface='eth0'):
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ARP))
    sock.bind((iface, ETH_P_ARP))

    arp_request = ARP(src=src_ip, dst=dst_ip)
    print(arp_request)

    frame = Ether(src = sock.getsockname()[-1], dst = BROADCAST,
                  payload = arp_request)
    sock.send(frame.to_stream())

    while 1:
        try:
            eth = Ether.from_stream(sock.recv(1600))
            arp_reply = eth.payload

            if arp_reply.hw_dst == frame.src:
                print(arp_reply)
                break

        except DissectionError:
            print(".")


if len(sys.argv) != 3:
    print(__doc__ % sys.argv[0])
    sys.exit()

main(sys.argv[1], sys.argv[2])
