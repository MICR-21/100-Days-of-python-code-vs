# """coffee machine"""
# """Make 3 hot flavours of coffee espresso, cappuccino and latte."""
# """Expresso: 50ml water, 18g coffee beans, 0ml milk, $1.50"""
# """Cappuccino: 150ml water, 24g coffee beans, 100ml milk, $2.50"""  
# """Latte: 100ml water, 24g coffee beans, 100ml milk, $3.00"""
# """Coffee machine has 300ml water, 100g coffee beans, 200ml milk."""
# """Coin Operated, american coins: $0.25, $0.10, $0.05, $0.01"""


# """Program Requirements:
# 1. Display the menu of coffee options to the user.  
# 2. CHeck suffiency of resources for the selected coffee option.
# 3. Prompt the user to select a coffee option."""

resources= {
    "water": 300,
    "coffee_beans": 100,
    "milk": 200,
    "money": 0.0
}

# Check resources
def check_resources(coffee_type):
    if coffee_type == "expresso":
        if resources["water"] < 50 or resources["coffee_beans"] < 18:
            return False
    elif coffee_type == "cappuccino":
        if resources["water"] < 150 or resources["coffee_beans"] < 24 or resources["milk"] < 100:
            return False
    elif coffee_type == "latte":
        if resources["water"] < 100 or resources["coffee_beans"] < 24 or resources["milk"] < 100:
            return False
    return True


machine_on = True    
while machine_on:
    coffee_type = input("What would you like? (expresso/cappuccino/latte): ").lower()
    if coffee_type == "off":
        print("Turning off the coffee machine.")
        exit()
        
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee Beans: {resources['coffee_beans']}g")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${resources['money']:.2f}")
        
    elif coffee_type == "espresso":
        if check_resources(coffee_type):
            print("Please insert coins.")
            quarters = int(input("How many quarters (25 cents)? "))
            dimes = int(input("How many dimes (10 cents)? "))
            nickels = int(input("How many nickels (5 cents)? "))
            pennies = int(input("How many pennies (1 cent)? "))
            total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        
            if total_money >= 1.50:
                resources["water"] -= 50
                resources["coffee_beans"] -= 18
                resources["money"] += 1.50
                print("Here is your expresso. Enjoy!")
                
            else:
                print("Sorry, that's not enough money. Money refunded.")
                
    elif coffee_type == "cappuccino":
        if check_resources(coffee_type):
            print("Please insert coins.")
            quarters = int(input("How many quarters (25 cents)? "))
            dimes = int(input("How many dimes (10 cents)? "))
            nickels = int(input("How many nickels (5 cents)? "))
            pennies = int(input("How many pennies (1 cent)? "))
            total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
            if total_money >= 2.50:
                resources["water"] -= 150
                resources["coffee_beans"] -= 24
                resources["milk"] -= 100
                resources["money"] += 2.50
                print("Here is your cappuccino. Enjoy!")              
            else:
                print("Sorry, that's not enough money. Money refunded.")
    elif coffee_type == "latte":    
        if check_resources(coffee_type):
            print("Please insert coins.")
            quarters = int(input("How many quarters (25 cents)? "))
            dimes = int(input("How many dimes (10 cents)? "))
            nickels = int(input("How many nickels (5 cents)? "))
            pennies = int(input("How many pennies (1 cent)? "))
            total_money = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
            if total_money >= 3.00:
                    resources["water"] -= 100
                    resources["coffee_beans"] -= 24
                    resources["milk"] -= 100
                    resources["money"] += 3.00
                    print("Here is your latte. Enjoy!")
            else:
                    print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Sorry, not enough resources to make coffee.")
            
        

