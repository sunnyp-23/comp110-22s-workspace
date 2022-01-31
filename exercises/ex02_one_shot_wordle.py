"""One Shot Wordle - a closer step to Wordle."""

__author__ = "730487787"

secret_word: str = "python"
letters: int = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
guess_emoji: str = ""
word: str = input(f"What is your {letters}-letter guess? ")
# the word variable uses the variable "letters" so that the statement can still work even when the length of the word changes
yellow: bool = False
other_indices: int = 0

while len(word) != letters:
    word = str(input((f"That was not {letters} letters! Try again: ")))
# this step checks to make sure that the guess is the same number of letters as the secret word. if not, it prompts the user to guess a word with the right amount of characters

while index < letters:
    if word[index] == secret_word[index]:
        guess_emoji = guess_emoji + GREEN_BOX
# if the letter in the given index of the guessed word is the same as the secret word, then a green box will be printed
# if not, then the following else statement and loop will run through each index of the secret word successively to check if that letter is anywhere in the secret word
    else:
        while other_indices < letters and not yellow:
            if secret_word[other_indices] == word[index]:
                guess_emoji = guess_emoji + YELLOW_BOX
                yellow = True
            # if the letter at the index of the word is then in the word, a yellow box is printed and the loop is ended as the "yellow" statement of the while loop changes to a value of False
            else:
                other_indices = other_indices + 1
        if not yellow:
            guess_emoji = guess_emoji + WHITE_BOX
            # if the yellow variable doesn't change (meaning that no yellow box was printed), then instead a white box was printed to make up for that index space
    index = index + 1
    # the index number increases by one to check the next character in the guessed word
    yellow = False
    other_indices = 0
    # these values must be reset to make sure that when the corresponding loop runs again, it will start with the letter at the first index of the secret word
print(guess_emoji)
if word == secret_word:
    print("Woo! You got it!")
# this part is gauged by the actual word instead of the guess_emoji because the guess_emoji can change depending on the number of letters in the secret word
else:
    print("Not quite. Play again soon!")
