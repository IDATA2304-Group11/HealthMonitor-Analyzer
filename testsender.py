
import socket


HOST = '192.168.86.37'
PORT = 9235

packet = "2021-11-15 14:35:23;"
packet += "292;70;70;E89X-2JKL-5420-GH42"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(packet.encode("utf-8"))