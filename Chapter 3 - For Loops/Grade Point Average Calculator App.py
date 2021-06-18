'''
Description:
You are responsible for writing a program that will collect any number of grades from a user.
Your program will sort these grades numerically from highest to lowest and calculate the grade
point average of the user. Your program will then ask for the average the user desires and
calculate what the user must get on their next assignment to achieve this average. Lastly, your
program will make a copy of the users grades and allow them to alter one of their previous
grades to see how doing worse or better on an assignment would have changed their overall
average.

Example Output:
Welcome to the Average Calculator App
What is your name: mike

How many grades would you like to enter: 5
Enter grade: 72
Enter grade: 64
Enter grade: 80
Enter grade: 83
Enter grade: 77

Grades Highest to Lowest:
83
80
77
72
64

Mike's Grade Summary:
    Total Number of Grades: 5
    Highest Grade: 83
    Lowest Grade: 64
    Average: 75.2

What is your desired average: 79
Good luck Mike!
You will need to get a 98.0 on your next assignment to earn a 79.0 average.

Lets see what your average could have been if you did better/worse on an assignment.
What grade would you like to change: 64
What grade would you like to change 64 to: 80

New Grades Highest to Lowest:
83
80
80
77
72

Mike's New Grade Summary:
    Total Number of Grades: 5
    Highest Grade: 83
    Lowest Grade: 72
    Average: 78.4
Your new average would be a 78.4 compared to your real average of 75.2!
That is a change of 3.2 points!

'''
def enter_grades(n):
    return [int(input("Enter grade: ")) for _ in range(n)]

def print_grades(array):
    for num in array:
        print(num) 

def print_summary(arr):
    print("\nGrades Summary")
    print(f"\tTotal Number of Grades: {len(arr)}")
    print(f"\tHighest Grade: {max(arr)}")
    print(f"\tLowest Grade: {min(arr)}")

n=int(input("How many grades would you like to enter: "))

grades=enter_grades(n)
grades.sort(reverse=True)
print("\nGrades Highest to Lowest:")
print_grades(grades)

print_summary(grades)
avg1=sum(grades)/n
print(f"\tAverage: {avg1}")

desired_avg=float(input("\nWhat is your desired average: "))
print(f"You will need to get a {(desired_avg*(n+1))-sum(grades)} on your next assignment to earn a {desired_avg} average.")

grade_to_change=int(input("\nWhat grade would you like to change: "))
new_grade=int(input(f"What grade would you like to change {grade_to_change} to: "))
grades=[new_grade if x==grade_to_change else x for x in grades]
grades.sort(reverse=True)
print("\nNew Grades Highest to Lowest:")
print_grades(grades)

print_summary(grades)
avg2=sum(grades)/n
print(f"\tAverage: {avg2}")

print(f"\nYour new average would be a {avg2} compared to your real average of {avg1}!")
print(f"That is a change of {round(avg2-avg1,2)} points!")