# create laptop class with attributes like brand name, model name, price
# create two objects / instances of your laptop class

class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + " " + model_name

lap1 = Laptop("Dell", "Inspiron 3558", 40000)
lap2 = Laptop("Lenovo", "Ideapad Slim 3i", 95000)

print(lap1)
print(lap2)

print(lap1.brand_name)
print(lap2.brand_name)
print(lap1.laptop_name)
print(lap2.laptop_name)
