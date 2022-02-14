"""More advanced Wordle - 6 guesses for the word."""

__author__ = "730487787"


# Here, the code sets up the variables and the search of the character in the string.
def contains_char(string: str, character: str) -> bool:
    """Let's the user know if the character was found in the string."""
    assert len(character) == 1
    index: int = 0
    while index < len(string):
        if string[index] == character:
            return True
        else:
            index = index + 1
    return False


# Now, the colored boxes are used to inform the user on how to get closer to guessing the secret string.
def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji that codifies based on guess and secret."""
    assert len(guess) == len(secret)
    GREEN_BOX: str = "\U0001F7E9"
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ("")
    guess_index: int = 0
    while guess_index < len(guess):
        if secret[guess_index] == guess[guess_index]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[guess_index]) is True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        guess_index = guess_index + 1
    return emoji


# User is asked for the number of characters in a string and continues to guess until it is the right length. 
# They are prompted with an error message until the guess is the right length.
def input_guess(length: int) -> str:
    """Returns a prompt to continue guessng if original guess isn't the expected length."""
    phrase: str = input(f"Enter a {length} character word: ")
    while len(phrase) != length:
        phrase = input(f"That wasn't {length} chars! Try again: ")
    return phrase


# Here, the secret word is assigned and the user tries to guess the word with some feedback.
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    n: int = 1
    while n <= 6:
        print(f"=== Turn {n}/6 ===")
        guessed_word = input_guess(len(secret_word))
        emoji = emojified(guessed_word, secret_word)
        print(emoji)
        if guessed_word == secret_word:
            print(f"You won in {n}/6 turns! ")
            return
        else:
            n = n + 1
    print("X/6 - Sorry, try again tomorrow!")


# Finally, the main is run as a module
if __name__ == "__main__":
    main()