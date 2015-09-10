# string methods in pyton

str = "this is my testing string"

# str.capitalize()
# this returns a copy of the string with its first letter capitalized and the rest lowercase
capitalized_string = str.capitalize()

# str.casefold()
# casefold is similar to lowercase() but more agressive
str.casefold()

# str.center(width)
# this retuns the string centered in given length width
str.center(100)

# str.count(sub[, start[, end]])
# counts the amount of time the sub string is in the string
str.count(str[:1])

# str.encode(encoding="uft-8", errors="strict")
# This returns an encoded version of the string as bytes object. t
str.encode()

# str.endswith(suffix[, start[, end]])
# checks if a string end with the specfied suffix
str.endswith('ig')

# str.find(sub[, start[, end]])
# returns the lowest index of the sub
# this should only be used if you need the posiition
# to check if sub is a substring or not use the in operator
# 'Py' in "Python"
str.find('my')

