def Main():
	for step in range(5):
		print("This is the current step in the iteration: ", step)

	words = ["cat", "bat", "rat", "hat", "mat"]

	for word in words[:]:
		print(word)

	num = 0
	while num <= 0:
		num = int(input("Please enter a positive integer: "))
	print("congratulations you have enterd a positive integer")


if __name__ == '__main__':
	Main()