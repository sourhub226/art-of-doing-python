'''
Description:
You are responsible for writing a program that will convert any given speed in miles per hour to
a more metric friendly unit of meters per second. All calculations should be rounded to a set
decimal precision of 2 decimal places.

Example Output:
Welcome to the Miles Per Hour Conversion App
What is your speed in miles per hour: 55.8
Your speed in meters per second is 24.96.

'''

#1 mph = 0.4474 mps.
mph=float(input("Enter speed in miles per hour: "))
print(f"The speed in meters per second is {round(mph*0.4474,2)}")