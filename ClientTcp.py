import socket
import sys
# Create the socket

data = "Hello world Tcp!"


def start_connection(args):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        #Connect to server and send data

        sock.connect((args[1], int(args[2])))
        sock.sendall(bytes(data, "utf-8"))
        '''
        # Receive data
        received=str(sock.recv(1024), "utf-8")
        print(received)
        sock.close()
        '''

