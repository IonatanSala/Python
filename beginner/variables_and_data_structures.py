# Vriables and Data Structures in Python
my_number = 3
print(my_number) 	# 3

# change variable
my_number = 10
print(my_number)	# 10

# Python allows for 7 basic Arithmetic operators
#Addition + 
#Substration -
#Multiplication *
#Division /
#Modulo %
#Exponent **
#Floor Division //

# Lists
# Lists hold an arary of valus
# We declare a list with the square brackets
# nums = []

nums = [] 	# this creates a list

# add values to the list
nums.append(40)
nums.append('this is a string that is put into our nums list')
nums.append(20.4)

# dictionaries
# They work similar to lists, uses hash map
# store a key and value to that key
# they are very similar to objects in javascript
services = {
	'ftp': 21,
	'ssh': 22,
	'smtp': 25,
	'http': 80
}
