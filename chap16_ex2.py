# applying 40% offer

class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance_variables - unique for every class object
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + " " + model_name

    def apply_discount(self, percentage):
        return (self.price - (self.price*percentage)/100) 

lap1 = Laptop("Dell", "Inspiron 3558", 40000)
lap2 = Laptop("Lenovo", "Ideapad Slim 3i", 95000)

print(lap1.apply_discount(10))
print(lap2.apply_discount(40))

