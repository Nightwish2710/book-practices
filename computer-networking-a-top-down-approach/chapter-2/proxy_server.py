import socket

import const


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', const.PORT))
server_sock.listen(1)

while True:
    print('Ready to serve...')
    connection_sock, addr = server_sock.accept()

    try:
        msg = connection_sock.recv(2048)

        file_name = msg.split()[1].decode().partition('/')[2][1:]
        print(file_name)
        with open(file_name[1:], 'r') as f:
            data = f.readlines()

        connection_sock.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        for line in data:
            connection_sock.send(line.encode())

        print('OK!')
    except IOError:
        connection_sock.send('HTTP/1.1 400 Not Found\r\n\r\n'.encode())
    finally:
        connection_sock.close()

server_sock.close()
