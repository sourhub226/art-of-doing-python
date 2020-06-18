'''
Description:
You are responsible for writing a program that will calculate the hypotenuse and area of a right
triangle given its two bases. Your program will round all calculations to a precision of three
decimal places and provide a summary of the mathematical results.

Example Output:
Welcome to the Right Triangle Solver App
What is the first leg of the triangle: 20
What is the second leg of the triangle: 40.5
For a triangle with legs of 20 and 40.5 the hypotenuse is 45.169.
For a triangle with legs of 20 and 40.5 the area is 405.0.
'''

import math
side1=float(input("Enter length of side 1: "))
side2=float(input("Enter length of side 2: "))
hypo=round(math.sqrt(side1**2+side2**2),3)
area=round(0.5*side1*side2,3)
print(f"Hypotenuse = {hypo}\nArea = {area}")
