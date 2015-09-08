# to delcare a list do the following
my_list = list()
# or
my_list = []

my_list = [1,2,3,5,4,6,7,8]

# methods that can be used on lists

# append(x)
# this adds a single element to the end of a list
my_list.append(9)

# extend(L)	
# this merges antoher list L to the end
my_list.extend(list([10,20,30,40]))

# inser(i, x)
# inserts element 'x' at position i
lenght_of_my_list = len(my_list) # gets the length of my_list
my_list.insert(lenght_of_my_list,50)

# remove(x)	
# this removes the first occurance of x
my_list.remove(20) # removes 20 from the list

# pop()
# removes the last element in the list
my_list.pop()

# index(x)
# returns the first index of the value, throws an error otherwise
my_list.index(10)

# count(x)
# counts the number of occurences of an element x
my_list.count(4)

# sort()
# sorts the list
my_list.sort()

# reverse()
# reverses the list
my_list.reverse()

print(my_list)




