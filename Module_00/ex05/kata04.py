# The kata variable is always a tuple that contains, in the following order:
# • 2 non-negative integer containing up to 2 digits
# • 1 decimal
# • 1 integer
# • 1 decimal

# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print("module_{0:02}, ex_{1:04} : {2}, {3}, {4}".format(*kata))