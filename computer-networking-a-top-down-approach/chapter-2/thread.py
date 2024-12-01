import socket
import threading

import const


def web_process(connection_sock):
    try:
        msg = connection_sock.recv(2048)

        file_name = msg.split()[1].decode().partition('/')[2][1:]
        print(file_name)
        with open(f'{file_name}', 'r') as f:
            data = f.readlines()

        connection_sock.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        for line in data:
            connection_sock.send(line.encode())

        print('OK!')
    except IOError:
        connection_sock.send('HTTP/1.1 400 Not Found\r\n\r\n'.encode())
    finally:
        connection_sock.close()


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', const.PORT))
server_sock.listen(10)

while True:
    try:
        print('Ready to serve...')
        connection_sock, addr = server_sock.accept()
        thread = threading.Thread(target=web_process, args=(connection_sock,))
        thread.start()
    except KeyboardInterrupt:
        print('Close serve...')
        server_sock.close()
        break
