# my_favorite_function = add
# print(my_favorite_function(2,3))
import os
import art
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def add (n1,n2):
    return n1+n2

def subtract (n1,n2):
    return n1-n2

def multiply (n1,n2):
    return n1*n2

def divide (n1,n2):
    return n1/n2 if n2 != 0 else "Cannot divide by zero"

"""add the 4 fucntions to a dictionary as the values"""
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
} 
print(art.logo)

def calculator():
    num1 = float(input("Enter the first number: "))
    is_continue = True
    while is_continue:
        for choice in operations:
            print(choice)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the second number: "))
        if operation_symbol == "+":
            result = operations["+"](num1,num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        elif operation_symbol == "-":
            result = operations["-"](num1,num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        elif operation_symbol == "*":
            result = operations["*"](num1,num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        elif operation_symbol == "/":
            result = operations["/"](num1,num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")
        again = input("Do you want to continue? Type 'y' for yes or 'n' for no: ")
        if again == "y":
            is_continue = True
        elif again == "n":
            cls()
            calculator()

calculator()



    
           
