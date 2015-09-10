import socket

def Main():
	host = '0.0.0.0'	# loopback address (the address of your machine)
	port = 5000			# when someone connects to this machine through this port, it will go to this program

	s = socket.socket()		# 
	s.bind((host, port))	# 

	s.listen(1)	# listen for one connection at a time

	c,addr = s.accept()	# accepted a connection, which also returns a new socket
	print("Connection from: " + str(addr))
	while True:
		data = c.recv(1024).decode('utf-8')	# recive 1024 raw data, so you have to decode
		if not data: # if there is no data from client
			break
		print("From connected user: " + data )
		data = data.upper()
		print("Sending: " + data)
		c.send(data.encode('utf-8'))	# encode back int raw bytes
	c.close()


if __name__ == "__main__":
	Main()