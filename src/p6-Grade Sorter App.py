'''
Description:
You are responsible for writing a program that will collect four grades from a user. Your
program will then sort these grades from highest to lowest. Then, your program will simulate
dropping the lowest two grades the user entered. Lastly, it will comment on the users highest
grade.

Example Output:
Welcome to the Grade Sorter App
What is your first grade (0-100): 82
What is your second grade (0-100): 95
What is your third grade (0-100): 100
What is your fourth grade (0-100): 61
Your grades are: [82, 95, 100, 61]
Your grades from highest to lowest are: [100, 95, 82, 61]
The lowest two grades will now be dropped.
Removed grade: 61
Removed grade: 82
Your remaining grades are: [100, 95]
Nice work! Your highest grade is a 100.
'''

grades=[]
grades.append(int(input("Enter first grade (0-100): ")))
grades.append(int(input("Enter second grade (0-100): ")))
grades.append(int(input("Enter third grade (0-100): ")))
grades.append(int(input("Enter fourth grade (0-100): ")))
print(f"Your grades are: {grades}")
grades.sort(reverse=True)
print(f"Your grades from highest to lowest are: {grades}")
grades.pop()
grades.pop()
print(f"After removing lowest 2 grades,\nThe remaining grades are: {grades}")
print(f"Your highest grade is {grades[0]}")