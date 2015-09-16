# A class is referred to as a Data Structure or Type
# Holds data and behaviours these are called Attributes and Methods
# We create multiple's from one definition

# Syntax: class MyClass

# Attributes
# Variables that belong to that class
# Always public ( can be accessed after the '.')
# MyClass.MyAttribute

# Methods
# Function that belong to a class 
# Either does something to he classes data or does something with the classes data

# Objects
# Objects are much like a variable, however hold a whole classes information inside
# Can creat multiple instance of an object/class, Hence 'Object'
# Can store an manipulate information inside the object, Much like we do with string class/object

class MyClass:
	number = 0
	name = "nonname"


def Main():
	# create an object of our class
	me = MyClass()
	me.number = 127
	me.name = "Jonatan Sala"

	friend = MyClass()
	friend.number = 3
	friend.name = "Igor"

	empty = MyClass()

	print("Name: " + me.name + " Number: " + str(me.number))
	print("Name: " + friend.name + " Number: " + str(friend.number))
	print("Name: " + empty.name + " Number: "+  str(empty.number))

if __name__ == '__main__':
	Main()