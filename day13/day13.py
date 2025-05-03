"""Steps in debugging
1. Describe the problem
2. Reproduce the problem
3. Use a debugger
4. Use print statements 
5. Check the code
6. Check the documentation  
7. Check for typos
8. Check for syntax errors
9. Check for logic errors
10. Check for runtime errors

"""
"""Debugging example
1. Describe the problem"""
# def my_function():
#     for i in range (1,21):
#         if i == 20:
#             print("you got it")
#             
# my_function()

"""2. Reproduce the problem"""
# from random import randint
# dice_images = [1,2,3,4,5,6]
# dice_num = randint(0,5)
# print(dice_images[dice_num])

# year = int(input("Enter a year: "))
# if year > 1980 and year < 1994:
#     print("You are a millennial")
# elif year >= 1994:

#     print("You are a Gen Z")


def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])
fizz_buzz(3)

