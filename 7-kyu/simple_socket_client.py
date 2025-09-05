import socket


def socket_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 1111))
    message = 'test'
    s.send(message.encode())
    response = s.recv(1024).decode()
    s.close()
    return response == message
