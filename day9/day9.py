# DICTIONARIES

# {Key: Value}
programming_dictionary = {
     "Bug":"An error in a program that prevents the program from running as expected ",
     "Function":"A piece of code that you can call over and over again",
     "Loop":"The action of doing something over and over again,"
     }
# print(programming_dictionary["Bug"])


# adding new element in dictionary
# programming_dictionary["Call"]= "This is a function you call"
# 
# programming_dictionary["Expression"] = "Statement that talks about a variable."
# print(programming_dictionary)

# empty dictionary
# empty_dictionary= {}

# whippig an exisiting dictionary
# programming_dictionary = {}

# print(programming_dictionary)

# Edit an item in a dictionary

# programming_dictionary ["Loop"] = "CHARLES"
# print(programming_dictionary)

# Loop through a dictionary
# for key in programming_dictionary:
    # prints the key
    # print(key)
    # prints the values
    # print(programming_dictionary[key])



# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': -95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for grade in student_scores:
#     if student_scores[grade] > 91:
#         student_grades[grade] = "Outstanding"
        
#     elif student_scores[grade] > 81 and student_scores[grade] < 90:
#         student_grades[grade] = "Expectations"
        
#     elif student_scores[grade] > 71 and student_scores[grade] < 80:
#         student_grades[grade] = "Acceptable"
        
#     elif student_scores[grade] < 70:
#         student_grades[grade] = "Fail"
    
# print(student_grades)



# capitals = {
#     "France":"Paris",
#     "Germany":"Berlin"
# }
# travel_log = {
#     "France":["Paris" , "Nice", "Oijon"],
#     "Germany": {
#             "cities_visites":["Stuttgart", "Berlin"],
#             "total_visits":2
#         },
#     "Portugal":{
#         "total_visits":8
#     }
    
# }
# print(travel_log["Germany"]["cities_visited"][2])

# # nested lists

# nested_lists = ["A","B",["C", "D"]]
# print(nested_lists[2][1]) 


# capitals= {
#     "France": "Paris",
#     "Germany":"Berlin"
# # }
# Nested ists

# travel_logs= {
#     "France" : {
#         "num_times_visited" : 8,
#         "cities_visited": 12,
#         },
#     "Germany": {
#         "cities_visited": ["Berlin","Stuttgart"],
#         "total_visits" :5
#     },
# }

# printing Stuttgart
# print(travel_logs["Germany"]["cities_visited"][1])

# priting Lille
# print(travel_logs["France"][1])

# nested_list = ["A","B",["C","D"]]
# printing D
# print(nested_list[2][1])