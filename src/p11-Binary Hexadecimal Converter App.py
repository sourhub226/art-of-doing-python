'''
Description:
You are responsible for writing a program that will generate binary and hexadecimal values from
1 up to a specified user value. Recall that decimal is a base 10 number system, binary is a
base 2 number system, and hexadecimal is a base 16 number system. Your program will use
list slicing to first only show a portion of these values. Your program will then loop through the
entire lists of decimal, binary, and hexadecimal values to show the relationship between
numbers of different bases

Example Output:
Welcome to the Binary/Hexadecimal Converter App
Compute binary and hexadecimal values up to the following decimal number: 12
Generating lists....complete!
Using slices, we will now show a portion of each list.
What decimal number would you like to start at: 4
What decimal number would you like to stop at: 7
Decimal values from 4 to 7:
4
5
6
7 
Binary values from 4 to 7:
0b100
0b101
0b110
0b111
Hexadecimal values from 4 to 7:
0x4
0x5
0x6
0x7
Press Enter to see all values from 1 to 12.
Decimal----Binary----Hexadecimal
----------------------------------------------------------
1----0b1----0x1
2----0b10----0x2
3----0b11----0x3
4----0b100----0x4
5----0b101----0x5
6----0b110----0x6
7----0b111----0x7
8----0b1000----0x8
9----0b1001----0x9
10----0b1010----0xa
11----0b1011----0xb
12----0b1100----0xc
'''

max_value=int(input("Compute binary and hexadecimal values up to the following decimal number: "))
decimal_list=list(range(1,max_value+1))

print("Using slices, we will now show a portion of the list.")
start_no=int(input("What decimal number would you like to start at: ") )
stop_no=int(input("What decimal number would you like to stop at: "))

print(f"Decimal values from {start_no} to {stop_no}:")
for dec in decimal_list[start_no-1:stop_no]:
    print(dec)

print(f"Binary values from {start_no} to {stop_no}:")
for dec in decimal_list[start_no-1:stop_no]:
    print(bin(dec))

print(f"Hexadecimal values from {start_no} to {stop_no}:")
for dec in decimal_list[start_no-1:stop_no]:
    print(hex(dec))

print(f"All values from 1 to {max_value}:")
print("Decimal\tBinary\tHexadecimal")
for dec in decimal_list:
    print(f"{dec}\t{bin(dec)}\t{hex(dec)}")
