# Networking is a huge field
# Networking is the concept of 2 programs communicating accros a network
# It can be client-client, client-server or event client to client

# Client - An end device interfacing with a human
# Server - A device providing a service for clients

# Networking paradigms

# Client/Server model, this is the most common
# Clients connect in to the server to get information they require
# Web browsers(client) connects to the Google Website(Server)

# Peer-to-Peer model
# Useful for services that don't have to be constantly available. (Skype, Game Servers)
# Clients connect to other clients without the use of a central server.
# (Is actually a Client/Server model at it's core, just client's are acting as a server and client)

# Terminology
# Address - An IP address, eg "127.0.0.1"
#	All computers connected to a network should have one
# Port - A port number, eg 5000
#	The tell the incoming data what program to go to
#	COMMON PORT NUMBERS
	# 20 & 21: File Transfer Protocol (FTP)
	# 22: Secure Shell (SSH)
	# 23: Telnet remote login service
	# 25: Simple Mail Transfer Protocol (SMTP)
	# 53: Domain Name System (DNS) service
	# 80: Hypertext Transfer Protocol (HTTP) used in the World Wide Web
	# 110: Post Office Protocol (POP3)
	# 119: Network News Transfer Protocol (NNTP)
	# 143: Internet Message Access Protocol (IMAP)
	# 161: Simple Network Management Protocol (SNMP)
	# 194: Internet Relay Chat (IRC)
	# 443: HTTP Secure (HTTPS)
	# 465: SMTP Secure (SMTPS)
# Port numbers 1 - 1024 are reserved for core protocols, Try to use something above 1024 but below 65535

# SOCKETS
# Sockets are the programming abstractions for connections.
# They allow us to communicate in a bidirectional manner from program to programm across a network
# Once the are connect or ready to transmit, we can use them to send data and receive data.
# They implement the ommon transport protocols TCP and UDP

# Socket methods
# socket(socket_family, socket_type), the constructor creates a new socket
# bind((hostname, port)) bind takes a tuple of a host address and a port
# listen() , this will start listening for TCP connections
# accept(), Accepts a connection when found. (returns a new socket

# On the client side we use a method connect() to request a connection with the listening server
# connect((hostname, port)), takes a turple of the address and port
# recv(buffer), this tries to grab data from a TCP connection. (Waits)
# The buffer size determines how many bytes of data to receive at a time
# send (bytes), attempts to sent the bytes given to it
# close(), Closes a socket/connection and frees the port

# TCP
# Transmission Control Protocol
# Reliable Connection based Protocol
#	This means that the protocols forms a connection with the other device and keeps the connection open until it's closed
#	If a piece of data is lost on its way throuhg the internet, the protocol will organise the data to be resent
#	The protocol also checks if the data is corrupt and that it arrives in an ordered manner
#	TCP is slower than other protocols due to all the checking and making sure all the data is there
# 	So its used for programs that require all the data to arrive
# Ordered & Error checked (simple checksum)
# Used by Web Browsers, Email, SSH, FTP, ect


