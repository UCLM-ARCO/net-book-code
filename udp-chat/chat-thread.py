#!/usr/bin/env python3
"usage: %s [--server|--client]"

import sys
import socket
import _thread
SERVER = ('', 12345)
QUIT = b'bye'


class Chat:
    def __init__(self, sock, peer):
        self.sock = sock
        self.peer = peer

    def run(self):
        _thread.start_new_thread(self.sending, ())
        self.receiving()
        self.sock.close()

    def sending(self):
        while 1:
            message = input().encode()
            self.sock.sendto(message, self.peer)

            if message == QUIT:
                break

    def receiving(self):
        while 1:
            message, peer = self.sock.recvfrom(1024)
            print("other> {}".format(message.decode()))

            if message == QUIT:
                self.sock.sendto(QUIT, self.peer)
                break


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__ % sys.argv[0])
        sys.exit()

    mode = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if mode == '--server':
        sock.bind(SERVER)
        message, client = sock.recvfrom(0, socket.MSG_PEEK)
        Chat(sock, client).run()

    else:
        Chat(sock, SERVER).run()
