"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730487787"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character")
    exit()
match: int = 0
print("Searching for " + character + " in " + word)

if character == word[0]:
    print(character + " found at index 0")
    match = int(match + 1)
if character == word[1]:
    print(character + " found at index 1")
    match = int(match + 1)
if character == word[2]:
    print(character + " found at index 2")
    match = int(match + 1)
if character == word[3]:
    print(character + " found at index 3")
    match = int(match + 1)
if character == word[4]:
    print(character + " found at index 4") 
    match = int(match + 1) 
if match == int(0):
    print("No instances of " + character + " found in " + word)
if match == int(1):
    print("1 instance of " + character + " found in " + word)
if match >= int(2):
    print(str(match) + " instances of " + character + " found in " + word)
