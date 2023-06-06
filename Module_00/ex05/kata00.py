# Put this at the top of your kata00.py file
# The kata variable is always a tuple and can only be filled with integer.
# kata = (1,) tuple with one element
kata = (19, 42, 21)

print("The", len(kata), "numbers are:", ', '.join(map(str, kata)))

# Only tuple and int
# kata = (1,)
# try:
# 	it = iter(kata)
# except:
# 	print("There is one number:", kata)
# else: