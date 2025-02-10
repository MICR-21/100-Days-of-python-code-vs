# def my_function():
#     result = 3*2
#     return result
# output = my_function()
# print(output)

# function with output
# converting to title case e.g cHarles to Charles

# def format_name(fname, lname):
#     formatted_name = fname.title() + " " + lname.title()
#     return formatted_name
# output = format_name("jOhn", "doe")
# print(output)


# function as input to another function
# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_2(function_1("hello"))
# print(output)

# multiple return values
# def format_name(fname, lname):
#     if fname == "" or lname == "":
#         return "You didn't provide valid inputs."  # return statement ends the function
#     formatted_name = fname.title() + " " + lname.title()
#     return formatted_name
# output = format_name(input("Enter your first name: "), input("Enter your last name: "))
# print(output)

# leap year
# def my_function():
#     result = 3*2
#     return result
# output = my_function()
# print(output)

# function with output
# converting to title case e.g cHarles to Charles

# def format_name(fname, lname):
#     formatted_name = fname.title() + " " + lname.title()
#     return formatted_name
# output = format_name("jOhn", "doe")
# print(output)


# function as input to another function
# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_2(function_1("hello"))
# print(output)

# multiple return values
# def format_name(fname, lname):
#     if fname == "" or lname == "":
#         return "You didn't provide valid inputs."  # return statement ends the function
#     formatted_name = fname.title() + " " + lname.title()
#     return formatted_name
# output = format_name(input("Enter your first name: "), input("Enter your last name: "))
# print(output)

# leap year
# def is_leap_year(year):
     # Write your code here. 
     # Don't change the function name
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             elif year % 400 != 0:
#                 return False
#         elif year % 100 != 0:
#             return True
#     elif year % 4 != 0:
#         return False
# year = int(input("Enter the year: "))
# print(is_leap_year(year))

# DocStrings- used for commenting functions. It is a multi-line
# string that is used to explain what the function does.
def format_name(fname, lname):
    """Take a first and last name and format it into a title case
    string."""
    if fname == "" or lname == "":
        return "You didn't provide valid inputs."
    formatted_name = fname.title() + " " + lname.title()
    return formatted_name
output = format_name(input("Enter your first name: "), input("Enter your last name: "))
print(output)