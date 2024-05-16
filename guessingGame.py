import random
secret_number = random.randint(1, 9)
print("Welcome to the Number Guessing Game!")
print("You have 5 chances to guess the number between 1 and 9.")
for attempt in range(5):
        guess = int(input("Guess the number: "))

        if (guess == secret_number):
            print("Congratulations! You guessed the correct number!")
        else:
            if (guess < secret_number):
                print("Try again! Your guess is too low.")
            else:
                print("Try again! Your guess is too high.")

else:
        print("Sorry, you've run out of guesses. The correct number was", secret_number)