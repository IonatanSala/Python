# C-Types - Python pretending to be C
# Fuzzing _  , breaking things



# There are 3 widely reconized levels of programming: low-level (Assembly),
# high-level (C), and scripting (Python, Perl, etc). Ther are a few important 
# characteristics of each:

	# low-level - closest to the processor, hardest to write/read, most efficient and powerful.

	# high-level - A comfortable middle ground, low-level enough to compile into Assemmly and get
	# some of the power, but there are some efficiency losses when the compiler optimizes poorly

	# scripting - Furthest from the processor, these usually require some sort of interpreter
	# (and are often called interpreted languages as a result), they're inefficient relative to low or high - level languages, but much easier to read a write

# The Python interpreter
	# A fully-fledged, Turing-complete virtual computer ( Not exactly, but it's easier to thing of it as one),
	# the Python Interpreter is what executes a python program
	# Can be used to quickly script a task.
	# Has a built in destructor and garbage-collector
	# Operates on a REP loop
		# R - read, take in a line of code
		# E - Evaluate, turn the code into something 
		# the computer can uderstand, and execute it.
		# P - Print, show the result ( Not going to print each individual line as you go)

# dir() - returns the list of names in the current scope
# dir(object) - list the object's attributes
# help() - starts the interactive "help" routing on an interpreter
# help(object) - Looks up the item as the name of a module, function, class, method, keyoword, or
# documentation topic, and help page is printed on the console

import socket

print(help(socket))
print(dir(socket))

def Main():

	host = ''
	port = 1337

	s = socket.socket()

	s.bind((host,port))
	s.listen(1)

	print(dir())

	# waiting for some input to come in
	conn, addr = s.accept()
	print("The folowing client connected: " + str(conn))
	print(conn.recv(1024).decode())
	
if __name__ == '__main__':
	Main()


	