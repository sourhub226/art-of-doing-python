'''
Description:
You are responsible for writing a program that will convert a given temperature in degrees
Fahrenheit to degrees Celsius and degrees Kelvin. Your program will round all conversions to a
precision of four decimal places. Lastly, your program will display the results in a convenient
table style format.

Example Output:
Welcome to the Temperature Conversion App
What is the given temperature in degrees Fahrenheit: 212.52
Degrees Fahrenheit:     212.52
Degrees Celsius:        100.2889
Degrees Kelvin:         373.4389
'''

fah=float(input("Enter temperature in degrees Fahrenheit: "))
cel=round((fah-32)*5.0/9.0, 4)
kel=round(cel+273.15, 4)
print(f"Degree Fahrenheit:\t{fah}\nDegree Celsius:\t\t{cel}\nDegree Kelvin:\t\t{kel}")