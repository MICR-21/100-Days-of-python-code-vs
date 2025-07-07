"""Class is a Bleuprint"""

# syntax
# Class Car:

class User:
    """Constructor used to initialize attributes"""
    def __init__(self, id,name):
        self.id = id
        self.name = name
#         Provide default values
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1




Maina = User("001","Charles")
Tevin = User("002","Tevin")
Maina.follow(Tevin)
print(Tevin.followers)
print(Tevin.following)

print(Maina.followers)
print(Maina.following)