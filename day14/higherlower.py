import art
import gamedata
print(art.logo)
import random
first_choice = random.choice(gamedata.data)
second_choice = random.choice(gamedata.data)
score = 0
is_game_over = False
print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
print(art.vs)
print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")

while not is_game_over:
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    correct = 'a' if first_choice['follower_count'] > second_choice['follower_count'] else 'b'

    if user_input == correct:
            score += 1
            print(f"You are correct! Your current score is {score}.")
            first_choice = second_choice
            second_choice = random.choice(gamedata.data)
            print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
            print(art.vs)
            print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")

    else:
            print(f"Sorry, that's wrong. Your final score is {score}.")
            is_game_over = True





