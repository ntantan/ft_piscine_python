try:
	x = 1 / 0
except ZeroDivisionError:
	x = 0
finally:
	x = x + 1

print(x)