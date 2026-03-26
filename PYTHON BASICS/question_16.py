#Number Guessing Game
import random

best_score = None  

while True:
    number = random.randint(1, 100)
    attempts = 7
    used_attempts = 0

    print("\n I picked a number between 1 and 100")
    print("You have 7 attempts. Let's go!\n")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        used_attempts += 1
        attempts -= 1

        if guess == number:
            print(f"\n Correct! You guessed in {used_attempts} attempts.")

            # best score tracking
            if best_score is None or used_attempts < best_score:
                best_score = used_attempts
                print(" New Best Score!")
            else:
                print(f" Best Score so far: {best_score} attempts")

            break

        elif guess > number:
            print("Too high!")
        else:
            print(" Too low!")

        
        if abs(guess - number) <= 5:
            print(" Very close! Within 5!")

        if attempts > 0:
            print(f"Attempts remaining: {attempts}\n")
        else:
            print(f"\n You lost! The number was {number}")

    # ask to play again
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing ")
        break