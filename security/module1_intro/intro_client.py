import socket

def Main():

	host = ''
	port = 1337

	s = socket.socket()
	s.connect((host, port))
	s.send("Hi how are your".encode())


if __name__ == '__main__':
	Main()