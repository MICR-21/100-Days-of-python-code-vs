easy_turns = 10
hard_turns = 5


def check_answer(user_guess, choice, attempts):
    """Check the user's guess against the choice and provide feedback."""
    if user_guess < choice:
        print("Too low.")
        return attempts - 1
        user_guess = int (input("Make a guess: "))
    elif user_guess > choice:
        print("Too high.")
        return attempts - 1
        user_guess = int (input("Make a guess: "))
    else:
        print(f"You got it! The answer was {choice}.")
        exit()

def set_difficulty():
    """set the difficulty level and return the number of attempts."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return easy_turns
    elif difficulty == "hard":
        return hard_turns
    else:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
    exit()
    
def number_game():
    """Main function to run the number guessing game."""
    print("Welcome to the Number Game!")
    print(art.logo)
    choice = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    import random
    import art
    attempts = set_difficulty()
    turns = 0
    while turns !=choice:
        print(f"You have {attempts} attempts to guess the number.")
        user_guess = int (input("Make a guess: "))
        attempts = check_answer(user_guess, choice, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            exit()
        
number_game()

