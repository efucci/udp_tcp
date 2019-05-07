import socket
from threading import Thread


def udp_listener(ip, port):
    print("Init UDP Socket")
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((ip, port))

    try:
        while True:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            print('received message:', data.decode())
    except Exception as e:
        print(e)

    sock.close()


def tcp_listener(ip, port):
    print("Init TCP Socket")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection address:', addr)

    try:
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            print('received data:', data.decode())
            conn.send(data)  # echo
    except Exception as e:
        print(e)

    conn.close()


IP = '127.0.0.1'

TCP_PORT = 5005
UDP_PORT = 5004

BUFFER_SIZE = 20  # Normally 1024, but we want fast response

tcp_thread = Thread(target=tcp_listener, args=(IP, TCP_PORT))
udp_thread = Thread(target=udp_listener, args=(IP, UDP_PORT))

tcp_thread.start()
udp_thread.start()

