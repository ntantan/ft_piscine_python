import sys

if len(sys.argv) <= 1:
	print("Error: No argument provided")
	sys.exit()

if len(sys.argv) > 2:
	print("Error: Too many arguments")
	sys.exit()

a = 0
try:
	a = int (sys.argv[1])
except:
	print("Error: Only ingegers please")
	sys.exit()

if a == 0:
	print("This is zero")
elif a % 2 == 0:
	print("This is even") 
else:
	print("This is odd")