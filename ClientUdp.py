import socket
import sys

MESSAGE = "Hello World Udp!"

def start_connection(args):


    ip = sys.argv[1]
    port = int(sys.argv[2])
    print("UDP target IP:", str(ip))
    print("UDP target port:", str(port))
    print("message:", MESSAGE)
    ServerAdddressPort=(ip,port)
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # UDP
    sock.sendto(bytes(MESSAGE, "utf-8"), ServerAdddressPort)
