"""
Description:
You are responsible for writing a program that simulates a thesaurus. Your program will present
a user with a list of words that your thesaurus contains. Based on the users choice, you will
randomly present them with a synonym for their chosen word. Lastly, your program will display
all of the potential synonyms for each word in the thesaurus.

Example Output 1:
Welcome to the Thesaurus App!
Choose a word from the thesaurus and I will give you a synonym.
Here are the words in the thesaurus:
    -hot
    -cold
    -happy
    -sad
What word would you like a synonym for: Hot
A synonym for hot is boiling.

Would you like to see the whole thesaurus (yes/no): yes
Hot synonyms are:
    - balmy
    - summery
    - tropical
    - boiling
    - scorching
Cold synonyms are:
    - chilly
    - cool
    - freezing
    - frigid
    - polar
Happy synonyms are:
    - content
    - cheery
    - merry
    - jovial
    - jocular
Sad synonyms are:
    - unhappy
    - downcast
    - miserable
    - glum
    - melancholy

Example Output 2:
Welcome to the Thesaurus App!
Choose a word from the thesaurus and I will give you a synonym.
Here are the words in the thesaurus:
    -hot
    -cold
    -happy
    -sad
What word would you like a synonym for: mad
I'm sorry, that word is not currently in the thesaurus.

Would you like to see the whole thesaurus (yes/no): no
I hope you enjoyed the program. Thank you!
"""
import random

thesaurus = {
    "hot": ["balmy", "summery", "tropical", "boiling", "scorching"],
    "cold": ["chilly", "cool", "freezing", "frigid", "polar"],
    "happy": ["content", "cheery", "merry", "jovial", "jocular"],
    "sad": ["unhappy", "downcast", "miserable", "glum", "melancholy"],
}

print("Words available in the thesaurus: ")
for key in thesaurus:
    print("\t-" + key)

word = input("Choose a word from the above thesaurus: ").strip().lower()

if word in thesaurus:
    print(f"A synonym for {word} is {random.choice(thesaurus[word])}.")
else:
    print("Word not available in thesaurus")

choice = input("\nDo you want to see the whole thesaurus? (yes/no): ").lower().strip()

if choice == "yes":
    for keys, values in thesaurus.items():
        print(f"\n{keys.capitalize()} synonyms:")
        for value in values:
            print("\t-" + value)
