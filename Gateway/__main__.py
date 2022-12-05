#!/usr/bin/python

import Server as Server

# Address of this application.
THIS_HOST = '192.168.86.37'
THIS_PORT = 9852


# Address of the main server.
SERVER_HOST = '192.168.86.37'
SERVER_PORT = 9235


# Booting the server.
server = Server.Server()
server.start()