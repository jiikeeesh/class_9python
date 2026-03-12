import random

# A list of words to choose from
words = ["python", "coding", "vowel", "computer", "logic"]
secret_word = random.choice(words)
guessed_letters = ""
turns = 6

print("--- Welcome to Word Guesser! ---")

while turns > 0:
    failed = 0
    
    # Using len() and a loop to show the word progress
    for i in range(len(secret_word)):
        char = secret_word[i]
        if char in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print("\n") # Just a new line for spacing

    # If failed is 0, the user won!
    if failed == 0:
        print("You Win! The word was:", secret_word)
        break

    guess = input("Guess a character: ").lower()
    guessed_letters += guess

    if guess not in secret_word:
        turns -= 1
        print(f"Wrong! You have {turns} more guesses.")

    if turns == 0:
        print("Game Over! The word was:", secret_word)