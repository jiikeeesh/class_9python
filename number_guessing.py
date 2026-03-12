import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = []  # We will store every guess here

print("--- Welcome to the Number Guessing Game! ---")
print("I'm thinking of a number between 1 and 50.")

while True:
    guess = int(input("Enter your guess: "))
    attempts.append(guess)  # Add the guess to our list

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        # Here is your len() function in action!
        total_guesses = len(attempts)
        print(f"Congratulations! You found it in {total_guesses} tries.")
        print("Your guess history was:", attempts)
        break