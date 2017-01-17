import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET IPV4 socket
# socket.SOCK_STREAM tcp socket

clientSocket.connect(("www.google.com", 80))
# no http because port 80 is standard http port

request = "GET / HTTP/1.0\r\n\r\n"

clientSocket.sendall(request)

response = bytearray()
while True:
	part = clientSocket.recv(1024)
	if (part):
		response.extend(part)
	else:
		break
print response
