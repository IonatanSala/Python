# Files
# easy in python
# great way to store data
# great way to load information
# reading
# writing
# appending
# close the file AFTER

def Main():
	# open our file
	file = open("file_IO_example.txt", "r")
	for line in file:
		print(line.strip())
	# close our file
	file.close()

	# writing to the file

	# Make the user enter four words
	writin_file = open("file_IO_example.txt", "w")

	for i in range(1,5):
		writin_file.write(input("Please enter word number " + str(i) + ": ")+'\n')
	writin_file.close()

	# using the with statement
	words = ["another cat", "another sat", "another mat"]


	with open("words.txt", "w") as f:
		for word in words:
			f.write(word + '\n')

	# we don't have to colse becasue we used the with keyword
	# if the file doesn't exist it will be created

if __name__ == '__main__':
	Main()
