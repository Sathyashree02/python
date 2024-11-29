import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Higher!")
        elif user_guess > number_to_guess:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_number()
