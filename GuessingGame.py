import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def number_guessing_game():
    print(Fore.CYAN + "Welcome to the Number Guessing Game!")
    
    # Ensure user enters a name
    name = ""
    while not name.strip():
        name = input(Fore.LIGHTGREEN_EX + "Enter your name: ")
        if not name.strip():
            print(Fore.RED + "You must enter a name.")
    
    print(Fore.CYAN + f"Hello, {name}! Let's start the game.")
    
    number_to_guess = random.randint(1, 10)
    attempts = 5

    print(Fore.CYAN + "I have selected a number between 1 and 10. You have 5 attempts to guess it.")
    
    for attempt in range(1, attempts + 1):
        guess = None
        while guess is None:
            user_input = input(Fore.LIGHTGREEN_EX + f"Attempt {attempt}: Enter your guess: ")
            if user_input.strip():
                try:
                    guess = int(user_input)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number.")
            else:
                print(Fore.RED + "You must enter a guess.")
        
        if guess < number_to_guess:
            print(Fore.BLUE + "Your guess is too low.")
        elif guess > number_to_guess:
            print(Fore.BLUE + "Your guess is too high.")
        else:
            print(Fore.LIGHTGREEN_EX + f"Congratulations, {name}! You guessed the correct number {number_to_guess} in {attempt} attempts.")
            break
    else:
        print(Fore.RED + f"Sorry, {name}. You've used all {attempts} attempts. The correct number was {number_to_guess}. Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()
