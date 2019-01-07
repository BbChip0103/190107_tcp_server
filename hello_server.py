# TCP server example

MY_PORT = 38001

import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", MY_PORT))
server_socket.listen(5)

print ( "TCPServer Waiting for client on port "+str(MY_PORT) )

client_socket, address = server_socket.accept()
print ("I got a connection from ", address)

while:
	data = input('SEND MESSAGE:')
	client_socket.send(data.encode())

server_socket.close()
print("SOCKET closed... END")
