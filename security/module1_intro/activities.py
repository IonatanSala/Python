# define my main method
def Main():

	# Exercise 1
	# determines if input is even or odd
	def even_odd():	
		get_user_number = int(input("Please enter a number: "))
		# ternary operator
		is_even_or_odd = "even" if get_user_number % 2 == 0 else "odd"
		print(is_even_or_odd)

	# get the sum of 2 numbers
	def sumOfTwo():
		first_num = float(input("Enter your first number: "))
		second_num = float(input("Enter your second nummber: "))
		print(first_num + second_num)

	# given a list of integers determine how many are even
	def howManyAreEven():
		my_list = list(map(int, input("Please enter numbers followed by a space").strip().split()))
			
		even_counter = 0
		for list_int in my_list:
			if list_int % 2 == 0:
				even_counter += 1

		print(even_counter)
	
	# ansewrs the input string backwards
	def reverseMe():
		user_string = str(input("Enter your string: "))
		# [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
		reversed_string = user_string[::-1]
		print(reversed_string)

	even_odd()
	sumOfTwo()
	howManyAreEven()
	reverseMe()


if __name__ == '__main__':
	Main()