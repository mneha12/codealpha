import random

def choose_word():
    # List of possible words
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(display_word(word, guessed_letters))

    while attempts_left > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

# Run the game
hangman()
