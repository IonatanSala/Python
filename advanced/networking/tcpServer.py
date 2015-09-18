import socket

def Main():
	print('enter main function')
	host = '127.0.0.1'	# loopback address (the address of your machine)
	port = 5000			# when someone connects to this machine through this port, it will go to this program
	print('after host and port are declared')

	print('create socket')
	s = socket.socket()		# 
	print('bind host and port number to the socket')
	s.bind((host, port))	# 

	print('listen on that connection')
	s.listen(1)	# listen for one connection at a time

	print('accept connection and assign c and addr to that connected socket')
	c,addr = s.accept()	# accepted a connection, which also returns a new socket
	print('after accepted connection')
	print("Connection from: " + str(addr))
	while True:
		print('enter while true')
		print('waiting for data from the user for the next code to be executed...')
		data = c.recv(1024).decode('utf-8')	# recive 1024 raw data, so you have to decode
		print('data gotten')
		if not data: # if there is no data from client
			break
		print("From connected user: " + data )
		data = data.upper()
		print("Sending: " + data)
		c.send(data.encode('utf-8'))	# encode back int raw bytes
	c.close()


if __name__ == "__main__":
	Main()