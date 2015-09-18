# A regular Expression or RegEx for short is a Pattern matching Language.
# The Regular language was invented by American mathematician Stephen Kleene.
# Use for Searches , Find, Replace, validation.
# Most programming languges support RegEx and others require additional libraies

# The Expression is a string of characters. There is two types of characters Metacharacters which hace
# special meaning, and Regular characters which have literal meaning.
# Can be simple and easy to learn, Hosever takes long time to master and use andvanced expressions

# There is a few different algorithms that regular expressions can use. The most common beign a DFA or 
# (Deterministic Finite Automaton)
# The DFA Algorithm is modified to use a pattern to specify it's computaion rules
# The DFA algorithm takes O(2^m) to cnstruct the Regular Expression (Where m is the length of RegEx Pattern)
# then O(n) time to search a string of length n.

# Matching & Searching 
# Python gives us two base methods to use our regular expression with.
# match() - Checks to see if the expression matches the entire string
# search() - Checks to see if there is a match anywhere in the string

# Search and Replace
# Python implements search and replace in a nice little method called sub() (Substitute)
# sub(pattern, repl, string, max=)
# Sub takes pattern and a string to replace it with and a string to search through. You can limit the amount of replaces by overwritng the max variable

# Extra info
# When using the same pattern multiple times in a for lopp, make your program more efficient by
# compiling the expression. (Creating the expression takes the longes time and more cycles on the CPU)
# e.g
# 	myReg = re.compile(pattern)
#	result = myReg.match(string)


import re
import argparse

def Main():

	#line = "I understand regular expressions"

	## match method
	#matchResult = re.match('undersatnd', line, re.M | re.I)
	#if matchResult:
	#	print("Match found: " + matchResult.group())
	#else: 
	#	print("No match was found")


	#searchResult = re.search('understand', line, re.M | re.I)
	#if searchResult:
	#	print("Search found: " + searchResult.group())
	#else:
	#	print("nothing found in search")

	parser = argparse.ArgumentParser()
	parser.add_argument("word", help="Specify word to search for")
	parser.add_argument("fname", help="specify file to search")
	args = parser.parse_args()

	searchFile = open(args.fname)
	lineNum = 0

	for line in searchFile.readlines():
		line = line.strip('\n\r')
		lineNum += 1
		searchResult = re.search(args.word, line, re.M | re.I)
		if searchResult: 
			print(str(lineNum)+ ': ' + line)



if __name__ == '__main__':
	Main()