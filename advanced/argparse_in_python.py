# Argparse is a module that allows for neat and familiar option and argument parsing for our python prgrams
# Automatically generates the usage
# Has inbuilt help function
# Auto formats the output for the console

# It interfaces with the python system nodule to grab the arguments from the command line
# Supports checking and making sure required arguments are provided

# parser = argparse.ArgumentParser()
# parser.add_argument('num', help="help text", type=int)
# args = parser.parse_args()
# print args.num

# Positional arguments are required arguments that we need for our program to complete.
# Positional arguments do not require the dash(-) because it is not an option.
# in the case of the fibonacci program this is the number num to count up to

# Optionsal Arguments
# As their title indicates, the optional arguments are optional.
# The -h option is laready inbuilt by default
# We can create as many as we like and argparse will handle it
# Like the positional arguments the help will be automatically added to the help output.
# parser.add_argument("--quiet", help="help text", action="store_true")

# Mutually Excusive Arguments
# You can select one option or another option, but not both
# This can be done with a group
# Automatically generates an output telling the user can only pick one, should they try to use both

# create a program that calculates the nth fibionacci number

# Optional output number to file. "--output"
# Add a short option aswell. "-o"
# Add help for the optional output

import argparse

def fib(n):

		a, b = 0, 1

		for i in range(n):
			a, b = b, a+b

		return a

def Main():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-v', '--verbose', action="store_true")
	group.add_argument('-q', '--quite', action="store_true")
	parser.add_argument("num", help="The fibonacci number you wish to calculate.", type=int)
	parser.add_argument("-o", "--output", help="Output result to a file.", action="store_true")


	args = parser.parse_args()

	result = fib(args.num)

	if args.verbose:
		print("The " + str(args.num) + "th fib number is " + str(result))
	elif args.quite:
		print(result)
	else: 
		print("Fib("+ str(args.num) + ") = " + str(result))

	if args.output:
		f = open("fibonacci.txt", "a")
		f.write(str(result)+ "\n")
		f.close()





if __name__ == '__main__':
	Main()