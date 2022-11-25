

import socket
import microclient as client




THIS_HOST = ''
THIS_PORT = 58912

SERVER_HOST = '172.20.10.2'
SERVER_PORT = 9235


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((THIS_HOST, THIS_PORT))
    print(s.getsockname())
    s.listen(3)
    conn, addr = s.accept()

    with conn:
        print(f"Connected by: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = str(data.decode('utf-8'))
            client.send_data(SERVER_HOST, SERVER_PORT, data)
        s.close()