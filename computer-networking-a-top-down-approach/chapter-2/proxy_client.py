import socket

import const


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((const.HOST_NAME, const.PORT))

client_sock.send('GET http://hello.html HTTP/1.1\r\n'.encode())
data = 1

while data:
    data = client_sock.recv(2048)
    print(data.decode(), end='')

client_sock.close()
