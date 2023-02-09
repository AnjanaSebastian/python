import random

def play_game():
    print("Welcome to the number guessing game!")
    number = random.randint(1, 100)
    tries = 0
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        tries += 1
        
        if guess == number:
            print(f"You win! It took you {tries} tries.")
            break
        elif guess < number:
            print("The number is higher.")
        else:
            print("The number is lower.")

play_game()
