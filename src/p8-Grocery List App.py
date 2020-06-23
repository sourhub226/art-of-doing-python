'''
Description:
You are responsible for writing a program that will simulate a grocery shopping list. Your
program will start with two items on the shopping list, meat and cheese, and then allow a user to
add three new items to the list. To simulate shopping, your program will ask the user what item
they just purchased and then remove the item from the shopping list. Upon having only two
items in the shopping list, your program will inform the user that the store is out of a particular
item and prompt the user to replace the item with a new item. You will use the datetime library
to display the current date and time the shopping is taking place in mm/dd hh:mm format.

Example Output:
Welcome to the Grocery List App.
Current Date and Time: 11/3 2:31
You currently have Meat and Cheese in your list.

Type of food to add to the grocery list: bananas
Type of food to add to the grocery list: apples
Type of food to add to the grocery list: soup

Here is your grocery list:
['Meat', 'Cheese', 'Bananas', 'Apples', 'Soup']
Here is your grocery list sorted:
['Apples', 'Bananas', 'Cheese', 'Meat', 'Soup']

Simulating grocery shopping...
Current grocery list: 5 items
['Apples', 'Bananas', 'Cheese', 'Meat', 'Soup']

What food did you just buy: apples
Removing Apples from list...
Current grocery list: 4 items
['Bananas', 'Cheese', 'Meat', 'Soup']

What food did you just buy: Cheese
Removing Cheese from list...
Current grocery list: 3 items
['Bananas', 'Meat', 'Soup']

What food did you just buy: soup
Removing Soup from list...
Current grocery list: 2 items
['Bananas', 'Meat']

Sorry, the store is out of Meat.
What food would you like instead: fish
Here is what remains on your grocery list:
['Fish', 'Bananas']
'''

import datetime

time = datetime.datetime.now()
print(time.strftime("Current Date and Time: %m/%d %I:%M %p"))

food_list=["Meat","Cheese"]
print("You currently have Meat and Cheese in your list.\n")

for _ in range(3):
    food_list.append(input("Type of food to add to the grocery list: ").title())

print("\nHere is your grocery list:")
print(food_list)
print("Here is your grocery list sorted:")
food_list.sort()
print(food_list)

print("\nSimulating grocery shopping...")

for _ in range(3):
    buy_food=input("What food did you just buy: ").title()
    print(f"Removing {buy_food} from list...")
    food_list.remove(buy_food)
    print(f"Current grocery list: {len(food_list)} items")
    print(f"{food_list}\n")


print(f"Sorry, the store is out of {food_list.pop()}")
food_list.append(input("What food would you like instead: ").title())
print("\nHere is what remains on your grocery list:")
print(food_list)