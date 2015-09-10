# Python considers the following to be False

# None

# False

# zero of any numeric type, for example, 0, 0.0, 0j.

# any empty sequence, for example, '', (), [].

# any empty mapping, for example, {}.

# instances of user-defined classes, if the class defines a __bool__() or __len__() method, 
# when that method returns the integer zero or bool value False. [1]

# all(iterable)
# Returns True if all elements of the iterable are true
# or if the iterable is empty: Equivalent to:

def all(iterable):
	for element in iterable:
		if not element:
			print(element)
			return False
	return True

my_tuple = 1,2,3,4,7

are_all_true = all(my_tuple)

print(are_all_true)