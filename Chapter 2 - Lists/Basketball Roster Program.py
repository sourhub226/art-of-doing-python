'''
Description:
You are responsible for writing a program that will build and display a basketball roster based off
user input. Your program will then simulate an injury to a specific player in the roster and
prompt the user to update the roster. Upon updating the roster, your program will display the
final roster and wish the newly add player good luck.

Example Output:
W​elcome to the Basketball Roster Program
Who is your point guard: mike eramo
Who is your shooting guard: Klay Thompson
Who is your small forward: LEBRON JAMES
Who is your power forward: Anthony DaVis
Who is your center: kevin getman

Your starting 5 for the upcoming basketball season
    Point Guard: Mike Eramo
    Shooting Guard: Klay Thompson
    Small Forward: Lebron James
    Power Forward: Anthony Davis
    Center: Kevin Getman

Oh no, Lebron James is injured.
Your roster only has 4 players.
Who will take Lebron James's spot: lucas eramo

Your starting 5 for the upcoming basketball season
    Point Guard: Mike Eramo
    Shooting Guard: Klay Thompson
    Small Forward: Lucas Eramo
    Power Forward: Anthony Davis
    Center: Kevin Getman

Good luck Lucas Eramo you will do great!
Your roster now has 5 players.
'''


roster = [input("Who is your point guard: ").title()]
roster.append(input("Who is your shooting guard: ").title())
roster.append(input("Who is your small forward: ").title())
roster.append(input("Who is your power forward: ").title())
roster.append(input("Who is your center: ").title())

print(f"\nYour starting {len(roster)} for the upcoming basketball season:")
print(
    "\tPoint Guard:" ,roster[0],
    "\n\tShooting Guard:",roster[1],
    "\n\tSmall Forward:",roster[2],
    "\n\tPower Forward:",roster[3],
    "\n\tCenter:",roster[4]
)

removed_player=roster.pop(2)
print(f"\nOh no, {removed_player} is injured.")
print(f"Your roster only has {len(roster)} players.")
added_player=input(f"Who will take {removed_player}'s spot: ").title()
roster.insert(2,added_player)


print(f"\nYour starting {len(roster)} for the upcoming basketball season:")
print(
    "\tPoint Guard:" ,roster[0],
    "\n\tShooting Guard:",roster[1],
    "\n\tSmall Forward:",roster[2],
    "\n\tPower Forward:",roster[3],
    "\n\tCenter:",roster[4]
)

print(f"\nGood luck {added_player} you will do great!")
print(f"Your roster now has {len(roster)} players.")