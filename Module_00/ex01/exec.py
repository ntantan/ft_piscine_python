import sys

if len(sys.argv) <= 1:
	print("No arguments provided")
	sys.exit()

print(" ".join(sys.argv[1:])[::-1].swapcase())