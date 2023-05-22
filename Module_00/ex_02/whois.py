import sys

if len(sys.argv) <= 1:
	print("No argument provided")
	sys.exit()

if len(sys.argv) > 2:
	print("Too many arguments")
	sys.exit()

if not sys.argv[1].isdigit():
	print("Not a fucking digit")
	sys.exit()

if int(sys.argv[1]) == 0:
	print("This is zero")
elif int(sys.argv[1]) % 2 == 0:
	print("This is even") 
else:
	print("This is odd")