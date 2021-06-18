'''
Description:
You are responsible for writing a program that will simulate flipping a coin n number of times.
Your program will present the user an option to see the result of each individual flip. Your
program will also inform the user any time the number of heads flipped is equal to the number of
tails flipped. Upon completion of all flips, your program will provide a summary table that shows
the number and percentage of each flip.

Example Output 1:
Welcome to the Coin Toss App
I will flip a coin a set number of times.
How many times would you like me to flip the coin: 97
Would you like to see the result of each flip (y/n): n

Flipping!!!
At 2 flips, the number of heads and tails were equal at 1 each.
At 8 flips, the number of heads and tails were equal at 4 each.
At 10 flips, the number of heads and tails were equal at 5 each.
At 12 flips, the number of heads and tails were equal at 6 each.
At 14 flips, the number of heads and tails were equal at 7 each.
At 20 flips, the number of heads and tails were equal at 10 each.

Results Of Flipping A Coin 97 Times:
Side    Count   Percentage
Heads   42/97   43.3%
Tails   55/97   56.7%

Example Output 2:
Welcome to the Coin Toss App
I will flip a coin a set number of times.
How many times would you like me to flip the coin: 10
Would you like to see the result of each flip (y/n): YEAH

Flipping!!!
TAILS
HEADS
At 2 flips, the number of heads and tails were equal at 1 each.
TAILS
TAILS
HEADS
HEADS
At 6 flips, the number of heads and tails were equal at 3 each.
TAILS
HEADS
At 8 flips, the number of heads and tails were equal at 4 each.
HEADS
TAILS
At 10 flips, the number of heads and tails were equal at 5 each.

Results Of Flipping A Coin 10 Times:
Side    Count   Percentage
Heads   5/10    50.0%
Tails   5/10    50.0%

'''
import random
heads=tails=0

n=int(input("How many times would you like me to flip the coin: "))
choice=input("Would you like to see the result of each flip (y/n): ").lower()

print("Flipping!")

for x in range(n):
    coin_face=random.choice(["Heads","Tails"])
    if  coin_face=="Heads":
        if choice.startswith('y'):
            print("Heads")
        heads+=1
    if coin_face =="Tails":
        if choice.startswith('y'):
            print("Tails")
        tails+=1
    if heads==tails:
        print(f"At {x+1} flips, the number of heads and tails were equal at {heads} each.")


print(f"\nResults Of Flipping A Coin {n} Times:")
print("Side\tCount\tPercentage")
print(f"Heads\t{heads}/{n}\t{round(heads/n*100,2)}")
print(f"Tails\t{tails}/{n}\t{round(tails/n*100,2)}")