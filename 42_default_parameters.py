# normal function
def userinfo(firstname, lastname, age):
    print(f"your first name is {firstname}")
    print(f"your last name is {lastname}")
    print(f"your age is {age}")
userinfo("Tushar", "Makwana", 21)


# function with default parameter
def userinfo(firstname, lastname, age = 21): # in majority case last parameter become default 
    print(f"your first name is {firstname}")
    print(f"your last name is {lastname}")
    print(f"your age is {age}") # default age is 21 if user does not input
userinfo("Tushar", "Makwana")


# function with default parameter
# def userinfo(firstname, lastname="unknown", age): # this will give error # if we make age default then is works
#     print(f"your first name is {firstname}")
#     print(f"your last name is {lastname}")
#     print(f"your age is {age}")
# userinfo("Tushar", 21) # error SyntaxError: non-default argument follows default argument


def userinfo(firstname, lastname, age=None):
    print(f"your first name is {firstname}")
    print(f"your last name is {lastname}")
    print(f"your age is {age}")
userinfo("Tushar", "Makwana", 21)