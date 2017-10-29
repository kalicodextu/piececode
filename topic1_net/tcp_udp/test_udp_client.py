#! /use/bin/env python
# -*- coding: utf-8 -*-

import socket

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client.connect((TARGET_HOST, TARGET_PORT))

# client.send("GET / HTTP/1.1\r\nHOST: baidu.com\r\n\r\n")
client.sendto("AABBCC", (TARGET_HOST, TARGET_PORT))

# response = client.recv(4096)
data, addr = client.recvfrom(4096)

print data
