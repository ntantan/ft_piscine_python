import sys

def text_analyzer(string):
	if not isinstance(string, str):
		print("This function only allows string")
		return

	ponct = spaces = upper = lower = 0
	
	for letter in string:
		if letter.isupper():
			upper += 1
		elif letter.islower():
			lower += 1
		elif letter.isspace():
			spaces += 1
		elif not letter.isalnum():
			ponct += 1

	print("The text contains", len(string), "character(s):")
	print("-", str(upper), "upper letter(s)")
	print("-", str(lower), "lower letter(s)")
	print("-", str(ponct), "ponctuation mark(s)")
	print("-", str(spaces), "space(s)")

if len(sys.argv) <= 1:
	print("What is the text to analyze?")
	sys.exit()

if len(sys.argv) > 2:
	print("Error: Too many arguments")
	sys.exit()

text_analyzer(sys.argv[1])