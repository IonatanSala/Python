# input and output in python

# first lets get the user to enter his name
name = input("What is your name: ")

# strip the name of any whitespace
name = name.strip()

# print name
print(name)


# Lets make a simple addition calculator
first_number = int(input("Please enter your first number: "))
second_number = int(input('Thank you, now please eneter your second number: '))
answer = first_number + second_number
print("The answer is: " + str(answer))