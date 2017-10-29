#! /use/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

BIND_IP = "0.0.0.0"
BIND_PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((BIND_IP, BIND_PORT))
server.listen(5)

print "[*] Listening on %s:%d " % (BIND_IP, BIND_PORT)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print  "[*] Received: %s" % request

    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print "[*] Accepted connection from  %s:%d" % (addr[0], addr[1])

    client_handle = threading.Thread(target=handle_client, args=(client, ))
    client_handle.start()
