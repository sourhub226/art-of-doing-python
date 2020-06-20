'''
Description:
You are responsible for writing a program that will highlight the similarities and differences
between four different types of lists: a list of strings, a list of integers, a list of floats, and a list of
lists. For each list, your program will describe the data type of the list, the elements of the list,
and the data type of the first element in the list. Your program will then highlight the similarities
and differences between sorting a list numerically and alphabetically.

Example Output:
Summary Table
The variable num_strings is a <class 'list'>.
It contains the elements: ['15', '100', '55', '42']
The element 15 is a <class 'str'>.

The variable num_ints is a <class 'list'>.
It contains the elements: [15, 100, 55, 42]
The element 15 is a <class 'int'>.

The variable num_floats is a <class 'list'>.
It contains the elements: [2.2, 5.0, 1.245, 0.142857]
The element 2.2 is a <class 'float'>.

The variable num_lists is a <class 'list'>.
It contains the elements: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
The element [1, 2, 3] is a <class 'list'>.

Now sorting num_strings and num_ints...
Sorted num_strings: ['100', '15', '42', '55']
Sorted num_ints: [15, 42, 55, 100]
Strings are sorted alphabetically while integers are sorted numerically!

'''

num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]

print(f"The variable num_strings is a {type(num_strings)}")
print(f"It contains the elements: {num_strings}")
print(f"The element {num_strings[0]} is a {type(num_strings[0])}")

print(f"\nThe variable num_ints is a {type(num_ints)}")
print(f"It contains the elements: {num_ints}")
print(f"The element {num_ints[0]} is a {type(num_ints[0])}")

print(f"\nThe variable num_floats is a {type(num_floats)}")
print(f"It contains the elements: {num_floats}")
print(f"The element {num_floats[0]} is a {type(num_floats[0])}")

print(f"\nThe variable num_lists is a {type(num_lists)}")
print(f"It contains the elements: {num_lists}")
print(f"The element {num_lists[0]} is a {type(num_lists[0])}")

print("\nNow sorting num_strings and num_ints...")
num_strings.sort()
num_ints.sort()
print(f"Sorted num_strings: {num_strings}")
print(f"Sorted num_ints: {num_ints}")
print("Strings are sorted alphabetically while integers are sorted numerically!")