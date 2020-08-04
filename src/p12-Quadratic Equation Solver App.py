'''
Description:
You are responsible for writing a program that will display the solutions to any number of
quadratic equations. Your program will ask the user how many quadratic equations they would
like to solve, ask for the coefficients of the equation in the standard form of ax2 + bx + c = 0 ,
solve for x, and then display the solutions. Your program will allow for both real and complex
solutions.

Example Output:
Welcome to the Quadratic Equation Solver App.
A quadratic equation is of the form ax^2 + bx + c = 0
Your solutions can be real or complex numbers.
A complex number has two parts: a + bj
Where a is the real portion and bj is the imaginary portion.

How many equations would you like to solve today: 2

Solving equation #1
---------------------------------------------------------------
Please enter your value of a (coefficient of x^2): 1
Please enter your value of b (coefficient of x): 6
Please enter your value of c (coefficient): 9
The solutions to 1.0x^2 + 6.0x + 9.0 = 0 are:
x1 = (-3+0j)
x2 = (-3+0j)

Solving equation #2
---------------------------------------------------------------
Please enter your value of a (coefficient of x^2): 1
Please enter your value of b (coefficient of x): -5
Please enter your value of c (coefficient): 14.2
The solutions to 1.0x^2 + -5.0x + 14.2 = 0 are:
x1 = (2.5+2.819574435974337j)
x2 = (2.5-2.819574435974337j)
Thank you for using the Quadratic Equation Solver App. Goodbye.

'''

import cmath
print("A quadratic equation is of the form ax^2 + bx + c = 0")

n=int(input("How many equations would you like to solve today: "))

for i in range(n):
    print(f"\nEquation {i+1}")
    print('-'*20)
    a=float(input("Please enter your value of a (coefficient of x^2): "))
    b=float(input("Please enter your value of b (coefficient of x): "))
    c=float(input("Please enter your value of c (coefficient): "))

    x1=((-b)+(cmath.sqrt((b*b)-(4*a*c))))/(2*a)
    x2=((-b)-(cmath.sqrt((b*b)-(4*a*c))))/(2*a)

    print(f"\nThe solutions to ({a})x^2 + ({b})x + (c) = 0 are:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")