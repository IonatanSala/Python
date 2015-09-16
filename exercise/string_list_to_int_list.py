# Flatening out a list in python

my_string_list = ["123", ["234", "235", ["345", "543"]], ["543", "643"]]

def recursive_change_list(my_list, my_int_list=[]):
	for i in my_list:
		if type(i) == list:
			recursive_change_list(i)
		else:
			my_int_list.append(int(i))
	return my_int_list

def Main():
	my_int_list = recursive_change_list(my_string_list)
	print(my_int_list)

if __name__ == '__main__':
	Main()
