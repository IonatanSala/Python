# functions
# functions is a way of splittin our programs up
# group reuasable code
# imporves readability, debugging

# Creating a Main function
# Place where the program will start
# Good Practice/ design
# Useful when building complex mosules for other people to use



def present_yourself(name, age, gender):
	print("Hi my name is ", name , ", I am ", age, " years old and I am a ", gender)



def get_addition(first_num, second_num):
	return first_num + second_num



def get_int():
	first_num = int(input("Please enter your first number to be added: "))
	second_num = int(input("Please enter the second number to be added: "))

	result = first_num + second_num

	return result



def Main():
	present_yourself("Jonatan Sala", 20, "male")

	result = get_addition(10, 193)
	print(result)

	result_from_user_input = get_int()
	print(result_from_user_input)

if __name__ == '__main__':
	Main()