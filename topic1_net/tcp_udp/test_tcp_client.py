#! /use/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import threading

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 8080

def client_connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((TARGET_HOST, TARGET_PORT))
    client.send(time.asctime())
    response = client.recv(4096)
    print response

client_send = threading.Thread(target=client_connect)
client_send.start()
