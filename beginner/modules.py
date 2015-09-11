# Modules are collections of code written by other people
# There are standard modules that allow for interaction with the operating system and also 
# modules for networking and many more
# You can find a list of the standard library here: 
# http://docs.python.org/3/library/

# Importing
# To use a module we need to import it into our program
# We use the syntax ( this must go at the top of the page)
# 	import modulename
# Since we will be using the math module we have to use:
import math

def Main():
	try: 
		number = float(input("Please enter a number: "))
		number = math.fabs(number)
		print(number)
	except:
		print("You did not enter a number")


if __name__ == '__main__':
	Main()