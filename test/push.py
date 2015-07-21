import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9000)

try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

try:
    message = bytes('karltk 5832aadc015611e5b4d30024d7c74394 | 1432390606 10\n', 'UTF-8')
    sock.sendall(message)

    amount_received = 0
    amount_expected = 1

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)

finally:
    print('closing socket')
    sock.close()
