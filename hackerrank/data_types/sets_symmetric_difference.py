# the challenge on hackerrank.com
# https://www.hackerrank.com/challenges/sets

def Main():
	input_results = []
	for i in range(4):
		try:
			user_first_input = input().strip()
			print("This is the users input: " , user_first_input)
			print("the type is : ", type(user_first_input))
		except:
			print("An error occured while getting the input")

	my_map = map(int, input_results)

	for i in my_map:
		print(i)


if __name__ == '__main__':
	Main()