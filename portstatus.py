#!/usr/bin/env python3
#
# author:      monsterb (http://monsterb.github.io)
# discription: Port Status is a very simple Python 3 script to find out if a port is open or closed.
# email:       UNIX.S3C (at) gmail (dot) com
# filename:    portstatus.py
# version:     0.00

import socket
ip = input("Enter the ip: ")
port = eval(input("Enter the port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if s.connect_ex((ip, port)):
    print("Port", port, "is closed")
else:
    print("Port", port, "is open")
