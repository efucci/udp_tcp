import socket
import sys


MESSAGE = "Hello World!"

ip = sys.argv[1]
port = int(sys.argv[2])
print("UDP target IP:", str(ip))
print("UDP target port:", str(port))
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE, (ip, port))
