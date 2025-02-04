# Randomization
import random
# import my_module
# the function is randint(a,b)

# random_int= random.randint(1,10)
# print(random_int)
# print(my_module.my_fav_no)

# random.random() used for decimals/float
# random_number=random.random() *10
# print(random_number)



# HEADS OR TAILS

# random_number = random.randint(0,1)
# if random_number == 0:
#     print("Heads")
# else:
#     print("Tails")
    

# PYTHON LISTS
# country_list = ["Kenya","Ethopia","Uganda","Djibouti", "Eritrea","Tanzania"]

# replacing element in a list
# country_list[1]="Senegal"

# adding item to list 
# country_list.append("Somalia")

# extenting the list
# country_list.extend(["Angola", "Algeria","South Africa","Chad","Somalia"])

# removing item to list
# country_list.remove("Somalia")

# printing a list
# print(country_list)

# CODING CHALLENGE

# friends= ["Alice","Bob","Charlie","David","Emmanuel"]

# random choice is used to randomize strings

# friends_random = random.choice(friends)
# print(friends_random)

#  dirty_dozen = [
#                 "Strawberries","Spinach","kale","Nectaries","Apples"
#                 ,"Grapes","Peaches","Cherries","Pears","Tomatoes"
#                 ,"Celery","Potatoes"
#             ]
fruits = ["Strawberries","Nectaries","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables = ["Spinach","kale","Tomatoes","Celery","Potatoes"]
# nested list
dirty_dozen = [fruits, vegetables] 
print(dirty_dozen)