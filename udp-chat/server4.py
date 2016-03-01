#!/usr/bin/env python3
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import socket
import _thread
server = ('', 12345)
QUIT = b"bye"


class Chat:
    def __init__(self, sock, peer):
        self.sock = sock
        self.peer = peer

        _thread.start_new_thread(self.sending, ())
        self.receiving()

    def sending(self):
        while 1:
            message = input().encode()
            self.sock.sendto(message, self.peer)

            if message == QUIT:
                break

    def receiving(self):
        while 1:
            message, peer = self.sock.recvfrom(1024)
            print(message.decode())

            if message == QUIT:
                self.sock.sendto(QUIT, self.peer)
                break

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server)
    message, client = sock.recvfrom(0, socket.MSG_PEEK)
    Chat(sock, client)
