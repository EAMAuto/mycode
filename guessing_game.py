# ALWAYS import modules first!

import random

secret_number = random.randint(1,10)

guess = int(input ("Guess the number between 1 and 10: "))

if guess < 1 or guess > 10:
    print("Invalid guess. Please enter a number between 1 and 10.")

elif guess == secret_number:
    print("You guessed it! Great job")

elif guess > secret_number:
    print("Too High!")
    
elif guess < secret_number:
    print ("Too Low!")



