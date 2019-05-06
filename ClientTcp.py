'''
    Semplicissimo script che invia una stringa al server e attende una sua risposta.
    Lo script utilizza due parametri che sono : il primo l'indirizzo del server e il secondo che sarebbe la porta con cui contattarlo.
'''
import socket
import sys
# Create the socket

data= "Questo è stato scritto in Python\n\r"

def start_connection(args):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        #Connect to server and send data

        sock.connect((args[1],int(args[2])))
        sock.sendall(bytes(data,"utf-8"))

        # Receive data
        received=str(sock.recv(1024),"utf-8")
        print(received)
        sock.close()

if __name__ == '__main__':
    start_connection(sys.argv)
