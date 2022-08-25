# This is a guess the number game

import random
import time
print('Hello, What is your name?')
name = input()

while True:

	print('\n'+'Well ' + name + ', I am thinking of a number between 1 and 20')
	secretNumber = random.randint(1,20)
	print("You get 4 Guesses to Guess the number")
	for GuessTaken in range(1, 5):
		print('Take a guess')
		try:
			Guess = int(input())
			if Guess > secretNumber:
				print('Your guess is too high')
			elif Guess < secretNumber:
				print('Your guess is too low')
			else:
				break # This condition is for a correct Guess
		except:
			print('You didnt enter a valid number')

	if Guess == secretNumber:
		print('\n'+'Good job, ' + name + '! You guessed my number in ' + str(GuessTaken) + ' guesses!')
	else:
		print('\n'+'Nope. The number I was thinking of was ' + str(secretNumber))
		
	print('Hope you Enjoyed playing the game')
	PlayAgain = input('\n'+'Do you want to play again? (Y or N)'+'\n')
	PlayAgain = PlayAgain.upper()
	try:
		if(PlayAgain == 'Y' or PlayAgain == 'YES'):
			print('All the best '+name)
			time.sleep(3)
		elif(PlayAgain == 'N' or PlayAgain == 'NO'):
			print('Thank You for playing the game '+name)
			time.sleep(3)
			break
		else:
			print('You did not enter a valid input, Closing the game')
			print('Thank You for playing the game '+name)
			time.sleep(3)
			break
			
	except:
		print('You did not enter a valid input, Closing the game')
		print('Thank You for playing the game '+name)
		time.sleep(3)
		break
