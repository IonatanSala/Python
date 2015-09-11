# exeption handling
# cathces errors
# avoids hard crashes
# good for user experiance
# commonly occurs when dealing with user input or file IO

# try/ except
# can surround anythin 
# only uses it around things that can fail
# syntax is as follows
	# try:
		# // do stuff here
	# except: 
		# // do this if any of the code in the try failed

def Main():
	# open a file that doesn't exist
	# try to open it
	try:
		file = open("blah.txt", "r")
		for line in file: 
			print(line.strip())
		file.close()
	# something went wrong so execute the following code
	except: 
		print("File could not be found or unable to be read")
	# this will always execute
	finally:
		print("Exiting")


if __name__ == '__main__':
	Main()