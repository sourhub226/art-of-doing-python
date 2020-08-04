'''
Description:
You are responsible for writing a program that will calculate the factorial of any given number.
Your program will display the mathematical relationship of the factorial. It will then use the math
library to compute the value of the given factorial. Lastly, your program will use its own
algorithm to compute the value of the given factorial and compare the results.

Example Output:
Welcome to the Factorial Calculator App

What number would you like to compute the factorial of? 10
10! = 1*2*3*4*5*6*7*8*9*10
Here is the result from the math library:
The factorial of 10 is 3628800!
Here is the result from my own algorithm:
The factorial of 10 is 3628800!
It is shown twice that 10! = 3628800 (with excitement)

'''

import math
n=int(input("Enter the number to compute the factorial of: "))
print(f'{n}! = ',end="")

for i in range(1,n):
    print(str(i), end="*")
print(str(n))

print(f"Answer using math library: {math.factorial(n)}")

fact=1
for x in range(2,n+1):
    fact*=x

print(f"Answer using own algorithm: {fact}")
