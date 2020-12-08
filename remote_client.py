import socket
import os 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

IP_address = "IP do servidor" 
Port = 9999

server.connect((IP_address, Port))  
  
while True:
    comando = str(input(": "))
    server.send(comando.encode("utf-8"))
    reposta = server.recv(100)
    print(reposta)
    print()
 
server.close() 
