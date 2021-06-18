'''
Description:
You are responsible for writing a program that will simulate registering to vote. If a user is 18 or
older, your program will present them with a list of potential political parties to register for. Upon
choosing a party, your program will confirm that the user has registered and print a specific
message depending on the party joined.

Example Output 1:
Welcome to the Voter Registration App
Please enter your name: mike
Please enter your age: 16

You are not old enough to register to vote.

Example Output 2:
Welcome to the Voter Registration App
Please enter your name: mike
Please enter your age: 21

Congratulations Mike! You are old enough to register to vote.
Here is a list of political parties to join.
    - Republican
    - Democratic
    - Independent
    - Libertarian
    - Green
What party would you like to join: republican

Congratulations Mike! You have joined the Republican party!
That is a major party!

'''
parties=["Republican", "Democratic", "Independent", "Libertarian", "Green"]

age=int(input("Enter your age: "))

if age <18:
    print("You are not old enough to register to vote.")
else:
    print("Congratulations! You are old enough to register to vote.")
    print("Here is a list of political parties to join.")
    for party in parties:
        print(f"\t-{party}")

    choosen_party=input("\nWhat party would you like to join: ").capitalize()
    if choosen_party in parties:
        print(f"Congratulations! You have joined the {choosen_party} party!")
    else:
        print("Please choose proper party to join.")
