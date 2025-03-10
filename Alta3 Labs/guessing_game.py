# ALWAYS import modules first!

import random

secret_number = random.randint(1,10)




#WE WANT THE USER TO HAVE 3 ATTEMPTS!

attempts = 0

print(f"CHEATMODE: {secret_number}")

while attempts < 3:
    guess = input("Guess the number between 1 and 10: ")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid guess. Choose a numeral!")
        continue
    if guess < 1 or guess > 10:
        print("Invalid guess. Please enter a number between 1 and 10.")

    elif guess == secret_number:
        print("You guessed it! Great job")
        break
    elif guess > secret_number:
        print("Too High!")
    
    elif guess < secret_number:
        print ("Too Low!")
    
    attempts +=1


