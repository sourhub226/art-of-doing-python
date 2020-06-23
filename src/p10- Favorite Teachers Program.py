'''
Description:
You are responsible for writing a program that will create a list of a user’s favorite teachers. It
will display these teachers ranked (assuming the first teacher entered is the favorite, the second
teacher entered is the next favorite, ect…), alphabetically, in reverse alphabetical order, the top
two teachers, the next two teachers, the last favorite teacher, and the total number of favorite
teachers in the list. Your program will then add and remove teachers from this list, each time
displaying a similar summary.

Example Output:
Welcome to the Favorite Teachers Program
Who is your first favorite teacher: Eramo
Who is your second favorite teacher: ricco
Who is your third favorite teacher: gates
Who is your fourth favorite teacher: foote

Your favorite teachers ranked are: ['Eramo', 'Ricco', 'Gates', 'Foote']
Your favorite teachers alphabetically are: ['Eramo', 'Foote', 'Gates', 'Ricco']
Your favorite teachers in reverse alphabetical order are: ['Ricco', 'Gates', 'Foote', 'Eramo']

Your top two teachers are: Eramo and Ricco.
Your next two favorite teachers are: Gates and Foote.
Your last favorite teacher is: Foote.
You have a total of 4 favorite teachers.

Oops, Eramo is no longer your first favorite teacher. Who is your new FAVORITE teacher:
marley
Your favorite teachers ranked are: ['Marley', 'Eramo', 'Ricco', 'Gates', 'Foote']
Your favorite teachers alphabetically are: ['Eramo', 'Foote', 'Gates', 'Marley', 'Ricco']
Your favorite teachers in reverse alphabetical order are: ['Ricco', 'Marley', 'Gates', 'Foote',
'Eramo']

Your top two teachers are: Marley and Eramo.
Your next two favorite teachers are: Ricco and Gates.
Your last favorite teacher is: Foote.
You have a total of 5 favorite teachers.

You've decided you no longer like a teacher. Which teacher would you like to remove from you
list: eramo
Your favorite teachers ranked are: ['Marley', 'Ricco', 'Gates', 'Foote']
Your favorite teachers alphabetically are: ['Foote', 'Gates', 'Marley', 'Ricco']
Your favorite teachers in reverse alphabetical order are: ['Ricco', 'Marley', 'Gates', 'Foote']

Your top two teachers are: Marley and Ricco.
Your next two favorite teachers are: Gates and Foote.
Your last favorite teacher is: Foote.
You have a total of 4 favorite teachers.
'''

teachers=[]

def favourite():
    print(f"\nYour favorite teachers ranked are: {teachers}")
    print(f"Your favorite teachers alphabetically are: {sorted(teachers)}")
    print(f"Your favorite teachers in reverse alphabetical order are: {sorted(teachers,reverse=True)}")

    print(f"\nYour top two teachers are: {teachers[0]} and {teachers[1]}.")
    print(f"Your next two favorite teachers are: {teachers[2]} and {teachers[3]}.")
    print(f"Your last favorite teacher is: {teachers[-1]}.")
    print(f"You have a total of {len(teachers)} favorite teachers.")


teachers.append(input("Who is your first favorite teacher: ").title())
teachers.append(input("Who is your second favorite teacher: ").title())
teachers.append(input("Who is your third favorite teacher: ").title())
teachers.append(input("Who is your fourth favorite teacher: ").title())
favourite()

teachers.insert(0,input(f"\nOops, {teachers[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").title())
favourite()

teachers.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title())
favourite()