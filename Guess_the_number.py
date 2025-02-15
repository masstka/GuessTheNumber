import random  # Import random module

number_to_guess = random.randint(1, 100)  # Random number between 1 and 100

while True:

    user_guess = input("Guess the number between 1 and 100: ")

    if not user_guess.isdigit():  # Check if input is a number
        print("It's not a number!")
        continue

    user_guess = int(user_guess)

    if user_guess < number_to_guess:  # Too small
        print("Too small!")
    elif user_guess > number_to_guess:  # Too big
        print("Too big!")
    else:  # Correct guess
        print("You win!")
        break
