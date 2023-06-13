import random

print("""
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")
      
number = random.randrange(1, 100)
attempt = 0
while True:
	answer = input("What is your guess between 1 and 99 ?\n")
	if answer == "exit":
		print("Goodbye")
		break

	try:
		guess = int (answer)
	except:
		print("This is not a number")
	else:
		attempt += 1
		if guess > 99 or guess < 1:
			print("Number is not contained between 1 and 99")
		elif guess < number:
			print("Too low !")
		elif guess > number:
			print("Too high !")
		else:
			if number == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if attempt == 1:
				print("Congratulations! You got it on your first try!")
			else:
				print("Congratulations, you've got it!")
				print("You won in {} attempts!".format(attempt))
			break