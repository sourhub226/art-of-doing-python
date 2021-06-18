'''
Description:
You are responsible for writing a program that will get a message and a specific letter from a
user and then count the number of occurrences of that letter in the given message. You
program should count “H” and “h” as an occurence of h. Your program will then display a
message to the user stating the occurrences of the given letter.

Example Output:
Welcome to the Letter Counter App
What is your name:
mike
Hello Mike!
I will count the number of times that a specific letter occurs in a message.
Please enter a message: Hello, how are you doing today? I hope that you have a happy
holiday!
Which letter would you like to count the occurrences of: h
Mike, your message has 7 h's in it.
'''

msg=input("Enter the message: ").lower()
letter=input("Which letter would you like to count the occurrences of: ").lower()
print(f"Your message has {msg.count(letter)} {letter}'s in it.")
