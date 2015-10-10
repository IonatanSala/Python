def cal(num ,num2):

	symbol = str(input("Please enter your operator: "))

	my_dict = { "+": num + num2, "-": num - num2, "*": num * num2, "/": num / num2 }

	return my_dict[symbol]


def Main():

	print(cal(5, 10))

if __name__ == "__main__":
	Main()