from ClientTcp import start_connectionTCP
from ClientUdp import start_connectionUDP
ip="localhost"
TCP_PORT = 5005
UDP_PORT = 5004
print("Ciao")
a = input("Vuoi inviare con udp o tcp?")
if a == "tcp":
    start_connectionTCP(ip, TCP_PORT)
else:
    start_connectionUDP(ip, UDP_PORT)