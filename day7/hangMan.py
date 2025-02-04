import random
import hangmanArt
import hangmanWords
print(hangmanArt.logo)
chosen_word = random.choice(hangmanWords.word_list)
print(chosen_word)
is_guessed = False
lives = 6
correct_guess = []
while is_guessed == False:
    print(f"You have {lives} Left")
    guess = input("Guess the letter: " .lower())
    display = ""
    if guess in correct_guess:
        print("You guessed:"+guess+ " which you already guessed")
    
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(guess)
        elif letter in correct_guess:
            display += letter      
        else:
            display += "_"
    print("Word to guess: " + display)
    
    
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in chosen word")
        if lives == 0:
            is_guessed =True
            print("You Lose")
        
    if "_" not in display:
        is_guessed = True
        print("You Win")

    print(hangmanArt.stages[lives])
