# Put this at the top of your kata01.py file
# The kata variable is always a dictionary and can only be filled with strings.
kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

for key, value in kata.items():
	print(key, "was created by", value)
