import sys
import socket
import threading

class Syncer(object):
    def __init__(self, port):
        self.__server_thread(port)

    def __server_thread(self, port):
        def worker(sock):
            sock.listen(1)

            while True:
                connection, client_address = sock.accept()
                try:
                    while True:
                        print("READING")
#                        data = connection.recv(4)
                        line = connection.makefile().readline()
                        print("READ " + str(line))
                        if not line:
                             connection.sendall("1")
                             break
                finally:
                    print("CLOSING")
                    connection.close()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", port))

        t = threading.Thread(target=worker, args=(sock,))
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    s = Syncer(9000)
    sys.stdin.read()
    print("DONE")
