import sys
import string

if len(sys.argv) != 3:
	print("Need two arguments")
	sys.exit()

try:
	s = str (sys.argv[1])
	n = int (sys.argv[2])
except:
	print("Usage : filterwords.py [string] [int]")
	sys.exit()

s = s.translate(str.maketrans('', '', string.punctuation))
s = s.split(' ')
s = [word for word in s if len(word) > n]
print(s)