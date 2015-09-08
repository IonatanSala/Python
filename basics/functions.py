
# Declare the function fib()
def fib(n):
	a,b = 0, 1
	while a < n:
		print(a)
		a,b = b, a+b

# Invoke the function
fib(10)

# Declare a function that returns a function
def return_my_name(name):
	return "Hi, my name is " + name

name = return_my_name("Jonatan Sala")

# Print the name
print(name)

# Default Argument Values
# The default values are evaluated at the point of function definition in the defining scope
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
	ok = raw_input(prompt)
	while True:
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise OSError('You ran out of tries')
		print(complaint)

ask_ok("Do you want to quit: ")





