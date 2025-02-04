# def greet():
#     print("Hey")
#     print("How are you")
#     print("I am doing well!")
# greet()

# functions with inputs

# def my_function(something):
#     do this with something


# def greet_with_name(name):
#      print(f"Hey {name}")
#      print(f"How are you {name}")
#      print(f"I am doing well! {name}")

# greet_with_name("Charles")

# age= int(input("What is your age? \n"))
# def life_in_weeks(age):
#     life= 90
#     days_in_weeks = 90 - age
#     weeks_left = days_in_weeks * 52
#     print(f"You have {weeks_left} weeks left")
    
# life_in_weeks(age)

#Functions with more than one input
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# name = input("What is your name ?\n")
# location = input("Where is your location?\n")

# positional arguments
# greet_with(name, location)

# keyword arguments
# greet_with(name = name , location = location)

# def calculate_love_score(name1, name2):
#     combinedNames = (name1+name2).lower()
#     trueString = "true"
#     loveString = "love" 
#     trueScore = 0
#     loverScore = 0
#     for character in trueString:
#         trueScore += combinedNames.count(character)
#         realscore1 = str(trueScore)
    
#     for character in loveString:
#         loverScore += combinedNames.count(character)
#         realscore2 = str(loverScore)
        
#     loveScore = realscore1 + realscore2
#     print(loveScore)
# calculate_love_score("KanyeWest", "KimKardashian")







