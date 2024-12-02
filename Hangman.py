import random

def choose_word():
    words = ["python", "java", "swift", "javascript"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
            guessed_letters.append(guess)
        
        if attempts == 0:
            print(f"Game over. The word was: {word_to_guess}")

hangman()
