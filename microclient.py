'''
    ANALYZER

Represents a component of the application, which
is implemented in a Raspberry Pi Microcomputer.<p>

This program will be able to receive data from a
sensor. This data will be processed and wrapped
into a package which can be sent to the backend
part of the application.

@author 
    jorgenfinsveen
@version
    10-11-2022
@since
    10-11-2022
'''

# Modules
import socket

'''
    # Server IP address and port number.
    HOST = '10.24.90.151'
    PORT = 8888
'''

def send_data(host, port, data):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(data.encode("utf-8"))
