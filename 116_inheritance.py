class Phone: # base / parent class
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
    
    def make_call(self, phone_number):
        print(f"calling .... {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model}"
    
class Smartphone(Phone): # derived / child class
    def __init__(self, brand, model, price, ram, rom, camera):
        # two ways
        # Phone.__init__(self, brand, model, price) # uncommon way / dont use : at end

        super().__init__(brand, model, price) # dont pass self and dont use : at end
        
        self.ram = ram
        self.rom = rom
        self.camera = camera
    

# class Smartphone: # derived / child class
#     def __init__(self, brand, model, price, ram, rom, camera):
#         self.brand = brand
#         self.model = model
#         self._price = max(price,0)
#         self.ram = ram
#         self.rom = rom
#         self.camera = camera
    
#     def make_call(self, phone_number):
#         print(f"calling .... {phone_number}")

#     def full_name(self):
#         return f"{self.brand} {self.model}"


phone = Phone("nokia", 1100, 1000)
smartphone = Smartphone("oneplus", "5", 30000, "6 GB", "64 GB", "20 MP")
print(phone.full_name())
print(smartphone.full_name())