"""local vs global scope"""

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
    
# increase_enemies()
# print(f"enemies outside function: {enemies}")

"""Local scope"""

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

player_health = 10

"""Global Scope"""

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()
# print(player_health)

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# def create_enemy():
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)

"""Prime Number -> number divisible by 1 and itself """
# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             print("It's not a prime number")
#             break
#     else:
#         print("It's a prime number")
# is_prime(73)

"""Modifying Global Scope"""
# enemies = 1

# def increase_enemies(enemy):   
#     return enemy + 1
    
# increase_enemies()
# print(f"enemies outside function: {enemies}")  

"""Global Constants"""
pi = 3.1459
