print("Welcome to Treasure Island \n Your Mission is to find the Treasure.")
cross_road = input("You're at a cross road. Where do you want yo go? Type 'left' or 'right'\n ")

if cross_road == "right" :
    print("Fall into a hole. \n Game Over.")
    
if cross_road == "left":
    print("You have come to a lake. There is an island in the middle of th lake.")
    lake_option = input("Type 'wait' to wait for a boat. Type 'swim 'to swim across\n")
    if lake_option == "swim":
        print("Attacked by Trout. \n Game over")
    if lake_option == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        color_door = input("One red, One yellow and one blue. Which color do you choose? \n")
        if color_door == "red":
            print("Burned by fire. Game Over.")
        elif color_door == "Yellow":
            print("You Win!")
        elif color_door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")                    
    

















