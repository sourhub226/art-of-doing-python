'''
Description:
You are responsible for writing a program that will simulate logging into a business’s shipping
accounts software. Once logged in your program will display the current costs of shipping x
amount of items. Based on the number of items shipped, the cost to ship each item will vary.
Once the cost to ship an item is set, your program will calculate the cost of shipping the entire
order. Upon confirmation of the order, your program will place the order and prepare the
shipment.

Example Output 1:
Welcome to the Shipping Accounts Program
Hello, what is your username: EramoM
Hello eramom. Welcome back to your account.

Current shipping prices are as follows:
Shipping orders 0 to 100:       $5.10 each
Shipping orders 100 to 500:     $5.00 each
Shipping orders 500 to 1000:    $4.95 each
Shipping orders over 1000:      $4.80 each

How many items would you like to ship: 867
To ship 867 items it will cost you $4291.65 at $4.95 per item.

Would you like to place this order (y/n): y
Okay. Shipping your 867 items.

Example Output 2:
Welcome to the Shipping Accounts Program
Hello, what is your username: allenj
Hello allenj. Welcome back to your account.

Current shipping prices are as follows:
Current shipping prices are as follows:
Shipping orders 0 to 100:       $5.10 each
Shipping orders 100 to 500:     $5.00 each
Shipping orders 500 to 1000:    $4.95 each
Shipping orders over 1000:      $4.80 each

How many items would you like to ship: 235
To ship 235 items it will cost you $1175.0 at $5.0 per item.

Would you like to place this order (y/n): n
Okay, no order is being placed at this time.

'''


print("Current shipping prices are as follows:")
print("\nShipping orders 0 to 100: \t\t$5.10 each")
print("Shipping orders 100 to 500: \t\t$5.00 each")
print("Shipping orders 500 to 1000: \t\t$4.95 each")
print("Shipping orders over 1000: \t\t$4.80 each")

quantity = int(input("\nHow many items would you like to ship: "))
if quantity < 100:
    cost = 5.10
elif quantity < 500:
    cost = 5.00
elif quantity < 1000:
    cost = 4.95
else:
    cost = 4.80

final_cost = round(quantity*cost, 2)
print(f"To ship {quantity} items it will cost you ${final_cost} at ${cost} per item.")

if input("\nWould you like to place this order (y/n): ").lower().startswith('y'):
    print(f"Okay. Shipping your {quantity} items.")
else:
    print("Okay, no order is being placed at this time.")