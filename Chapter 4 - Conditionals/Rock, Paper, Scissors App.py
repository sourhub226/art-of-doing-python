"""
Description:
You are responsible for writing a program that will simulate playing the classic game Rock,
Paper, Scissors against computer AI. Your program will ask the user how many rounds of the
game they would like to play, simulate each round, keep score, and determine an overall
winner. Your program will also print the classic phrases such as “Paper covers rock” or
“Scissors cut paper”.

Example Output:
Welcome to a game of Rock, Paper, Scissors
How many rounds would you like to play: 3

Round 1
Player: 0 Computer: 0
Time to pick...rock, paper, scissors: scissors
Computer: paper
Player: scissors
Scissors cut paper!
You win round 1.

Round 2
Player: 1 Computer: 0
Time to pick...rock, paper, scissors: PAPER
Computer: rock
Player: paper
Paper covers rock!
You win round 2.

Round 3
Player: 2 Computer: 0
Time to pick...rock, paper, scissors: Rock
Computer: rock
Player: rock
It is a tie, how boring!
This round was a tie.

Final Game Results
Rounds Played: 3
Player Score: 2
Computer Score: 0
Winner: PLAYER!!!

"""
import random

moves = ["rock", "paper", "scissor"]
p_score = c_score = 0


n = int(input("Enter no. of rounds: "))


def check_win(pmove, cmove):
    if (
        (pmove == "rock" and cmove == "scissor")
        or (pmove == "paper" and cmove == "rock")
        or (pmove == "scissor" and cmove == "paper")
    ):
        print("YOU WIN!\n")
        return "player"
    elif (
        (cmove == "rock" and pmove == "scissor")
        or (cmove == "paper" and pmove == "rock")
        or (cmove == "scissor" and pmove == "paper")
    ):
        print("COMPUTER WINS!\n")
        return "computer"
    else:
        print("TIE\n")


for i in range(n):
    print("Score:")
    print(f"Player: {p_score}")
    print(f"Computer: {c_score}")
    print(f"\nRound {i+1}")
    pmove = input("Enter your move (rock,paper,scissor): ").strip().lower()
    if pmove in moves:
        cmove = moves[random.randint(0, 2)]
        print(f"Your move: {pmove}")
        print(f"Computer's move: {cmove}")
        winner = check_win(pmove, cmove)
        if winner == "player":
            p_score += 1
        elif winner == "computer":
            c_score += 1

    else:
        print("Invalid move")
        print("COMPUTER WINS!")
        c_score += 1

print("FINAL SCORE:")
print(f"Player: {p_score}")
print(f"Computer: {c_score}")
