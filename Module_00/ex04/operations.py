import sys

if len(sys.argv) <= 2:
	print("Error: Need two arguments")
	sys.exit()

if len(sys.argv) > 3:
	print("Error: Too many arguments")
	sys.exit()

a = b = 0
try:
	a = int (sys.argv[1])
	b = int (sys.argv[2])
except:
	print("Error: Only ingegers please")
	sys.exit()

print("Sum:        ", a + b)
print("Difference: ", a - b)
print("Product:    ", a * b)

if b == 0:
	print("Quotient:   ", "ERROR (division by zero)")
	print("Remainder:  ", "ERROR (modulo by zero)")
else:
	print("Quotient:   ", a / b)
	print("Remainder:  ", a % b)