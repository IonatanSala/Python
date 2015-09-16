# concept of inheriting features from another class
# useful if tow or more classes share common attributes or methods
# can use methods from sthe usper class
# A more organized and modular way to desing programs. (Not all programs though)

# Terminology
# Base class or Supper class - The class that is inherited from
# Subclass - Inherits from a base/super class
# You can have subclasses of other subclasses

# Polymorphism
# Concept of dynamic methods chosen at runtime
# Subclasses must override the base classes method
# Useful for lists of diferent types of subclasses

# Adding Polymorphism 
# A talk method which will do something different for each pet
# The list will be a list of Pet classes because both Dogs and cats are Pet classes

class Pet:
	# constructor 
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self):
		raise NotImplementedError("Subclass must implement abstract method")



# Cat inherites from Pet
class Cat(Pet):
	def __init_(self, name, age):
		super().__init__(name, age) # your can run super class methods 

	def talk(self):
		return "Meowww"

class Dog(Pet):
	def __init__(self, name, age):
		super().__init__(name, age)

	def talk(self):
		return "Woof"


def Main():
	#thePet = Pet("Pet", 1)
	#jess = Cat("Jess", 3)

	#print("is jess a Cat?" + str(isinstance(jess, Cat)))
	#print("is jess a Pet?" + str(isinstance(jess, Pet)))
	#print("is thePet a Cat?" + str(isinstance(thePet, Cat)))
	#print("is thePet a Pet?" + str(isinstance(thePet, Pet)))

	pets = [Cat('Jess', 4), Dog("Maxi", 7)]

	for pet in pets:
		print("Name: " + pet.name + ", Age: " +str(pet.age) + " says: " + pet.talk())



if __name__ == '__main__':
	Main()

