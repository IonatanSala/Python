# any(iterable)
# this built in function, will return true if any element in the 
# iterable evaluates to True
# it is qquivalent to the following:

def any(iterable):
	for element in iterable:
		if element:
			print(element)
			return True
	return False

my_list = [False, None, 0, '', {}, [], (), 1]

is_any_true = any(my_list)

print(is_any_true)	# this will print True because of the 1 at the end of the my_list
