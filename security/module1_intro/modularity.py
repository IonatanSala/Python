# Write a program with a menu

# Accept and store a string

# Basic calculator

# Print the previously stored string

# Compare two numbers to determine the larger

# Remove a selected letter from a string

def accept_and_store():
	global user_string
	user_string = str(input("Please enter you string: "))

	return

def calculator():
	num = int(input("Please input your first number: "))
	sign = str(input("Action: "))
	num2 = int(input("Please enter your second number: "))

	my_dict = {
		"+": num + num2,
		"-": num - num2,
		"/": num / num2,
		"//": num // num2,
		"*": num * num2
	}

	result = my_dict[sign]
	print(result)
	return 

def print_previous():
	return

def compare_two_numbers():
	print("You are in the compare_two_numbers()")
	return

def remove_selected_letter():
	print("You are in the remove_selected_letter()")
	return


def Main():
	opt_list = [accept_and_store, calculator, print_previous, compare_two_numbers, remove_selected_letter]

	print("SELECT OPTION")
	print("1\tAccept and Store")
	print("2\tCalculator")
	print("3\tPrint Previous")
	print("4\tCompate 2 Numbers")
	print("5\tRemove Letter")

	user_option = int(input("-> "))
	user_option -= 1

	opt_list[user_option]()

	return 


if __name__ == '__main__':
	Main()