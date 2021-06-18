'''
Description:
You are responsible for writing a program that displays a multiplication table and exponentiation
table for any given number. Each table should show mathematical results for operations
performed with the given number and integers from 1 to 9. The program will then print a series
of messages to the user describing how cool mathematics truly is.

Example Output
Welcome to the Multiplication/Exponent Table App
What is your name: mike
What number would you like to work with: 2.35
Multiplication Table For 2.35
1.0 * 2.35 = 2.35
2.0 * 2.35 = 4.7
3.0 * 2.35 = 7.05
4.0 * 2.35 = 9.4
5.0 * 2.35 = 11.75
6.0 * 2.35 = 14.1
7.0 * 2.35 = 16.45
8.0 * 2.35 = 18.8
9.0 * 2.35 = 21.15

Exponent Table For 2.35
2.35 ** 1 = 2.35
2.35 ** 2 = 5.5225
2.35 ** 3 = 12.9779
2.35 ** 4 = 30.498
2.35 ** 5 = 71.6703
2.35 ** 6 = 168.4252
2.35 ** 7 = 395.7993
2.35 ** 8 = 930.1284
2.35 ** 9 = 2185.8017
Mike Math is cool!
mike math is cool!
Mike Math Is Cool!
MIKE MATH IS COOL!
'''

name=input("Enter your name: ")
num=float(input("Enter the number: "))

print(f"Multiplication table for {num}:")
for x in range(1, 10):
    print(f"{num} x {x} = {round(num*x,4)}")

print(f"\nExponent table for {num}:")
for x in range(1, 10):
    print(f"{num} ^ {x} = {round(num**x,4)}")

string=", Math is cool!"
print(f"{name.title()}{string}")
print(f"{name}{string}".lower())
print(f"{name}{string}".title())
print(f"{name}{string}".upper())