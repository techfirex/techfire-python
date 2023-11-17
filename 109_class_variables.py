class Circle():
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
    
    def calc_circumference(self):
        return 2*self.radius*self.pi
    

c1 = Circle(4,3.14)
c2 = Circle(5,3.14)
# here see 3.14 is same for every body which take memory at all places
print(c1.calc_circumference())


# lets add class variable in above example// class.class_variable
class Circle():
    pi = 3.14
    def __init__(self, radius, pi):
        self.radius = radius
    
    def calc_circumference(self):
        return 2*self.radius*Circle.pi
    
c3 = Circle(4,3.14)
print(c3.calc_circumference())


# we can do same in our previous example to apply 10% discount on all product for sale
class Laptop:
    discount = 10
    def __init__(self, brand_name, model_name, price):
        # instance_variables - unique for every class object
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + " " + model_name

    def apply_discount(self):
        return (self.price - (self.price*Laptop.discount)/100)

lap1 = Laptop("Dell", "Inspiron 3558", 40000)
lap2 = Laptop("Lenovo", "Ideapad Slim 3i", 95000)

print(lap1.apply_discount())
print(lap2.apply_discount())