
import random

words = ["python", "college", "laptop", "coding", "developer"]

secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.")

while incorrect_guesses < max_attempts:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame over! You ran out of attempts.")
    print("The correct word was:", secret_word)