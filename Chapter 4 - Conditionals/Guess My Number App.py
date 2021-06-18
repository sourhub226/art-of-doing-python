'''
Description:
You are responsible for writing a program that will play the classic “Hi Low” game. Your
program will randomly pick a number between 1 and 20. Users will then guess the number.
With each guess, your program will respond that the user’s guess is either too high or too low.
When the user guesses correct, or after 5 guesses, your program will end the game and
summarize the results.

Example Output 1:
Welcome to the Guess My Number App
Hello! What is your name: mike
Well Mike, I am thinking of a number between 1 and 20.

Take a guess: 15
Your guess is too low.

Take a guess: 20
Your guess is too high.

Take a guess: 19
Good job, Mike! You guessed my number in 3 guesses!

Example Output 2:
Welcome to the Guess My Number App
Hello! What is your name: MIKE
Well Mike, I am thinking of a number between 1 and 20.

Take a guess: 1
Your guess is too low.

Take a guess: 20
Your guess is too high.

Take a guess: 2
Your guess is too low.

Take a guess: 19
Your guess is too high.

Take a guess: 3
Your guess is too low.

Game Over. The number I was thinking of was 10.

'''

import random
win=False

print("I am thinking of a number between 1 and 20.")
num=random.randint(1,20)

for i in range(5):
    guess=int(input("\nTake a guess: "))
    if guess==num:
        print(f"Good job, You guessed my number in {i+1} guesses!")
        win=True
        break
    elif (guess-num) >=5:
        print("Your guess is too high.")
    elif abs(guess-num) <5:
        print("You are close.") 
    else:
        print("Your guess is too low.")

if not win:
    print(f"\nGame Over. The number I was thinking of was {num}.")