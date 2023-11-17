# operato overloading
# polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def __str__(self): # used by normal use to see output or something else
        return f"{self.brand} {self.model}"
    
    def __repr__(self): # used by python developer to do something // return object which we defined
        return f"Phone(\'{self.brand}\', \'{self.model}\', {self._price})"
    
    def __len__(self):
        return len(self.full_name())
    
    def __add__(self, other_object):
        return self._price + other_object._price
        # self means object first itself, example my_phone1
        # other_object means second one, example my_phone2
    

my_phone1 = Phone("nokia", "1100", 1000)
my_phone2 = Phone("nokia", "1600", 1200)

# operato overloading
# 2 + 3 = 5
# "abc" + "def" = "abcdef"
# similar multiplication, substaction etc operator can apply

# print(my_phone1 + my_phone2) # but in this case it can not do like this
# for that we have to add dunder method in our class to perform this, like __add__, __mul__ etc

print(my_phone1 + my_phone2)
# give sum of both prices


# polymorphism - many forms of any one thing
# operator overloading is example of polymorphism
# 2 + 3 = 5
# "abc" + "def" = "abcdef"
# in first + do sum of two
# in second + do joining of two string
# + operator do more than one thing

# method overriding is also example of polymorphism
# len function can find length of list, tuple, string etc also exmaple of this