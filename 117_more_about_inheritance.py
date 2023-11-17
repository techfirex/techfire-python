# can we derive more than one class from base class?
# multilevel inherihance
# method resolution order (MRO)
# method overriding (MO)
# isinstance() and issubclass()

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

# can we derive more than one class from base class? yes
# class Smartphone2(Phone): # derived / child class
#     def __init__(self, brand, model, price, ram, rom, camera):
#         # two ways
#         # Phone.__init__(self, brand, model, price) # uncommon way / dont use : at end

#         super().__init__(brand, model, price) # dont pass self and dont use : at end
#         self.ram = ram
#         self.rom = rom
#         self.camera = camera



# multilevel inherihance (Phone to Smartphone to FlagshipPhone)
class FlagshipPhone(Smartphone): # derived / child class
    def __init__(self, brand, model, price, ram, rom, camera, hybridsim):
        # two ways
        # Phone.__init__(self, brand, model, price) # uncommon way / dont use : at end

        super().__init__(brand, model, price, ram, rom, camera) # dont pass self and dont use : at end
        
        self.hybridsim = hybridsim

    def full_name(self): # this method is also in Phone class but we override with other modification
        return f"{self.brand} {self.model} and price is {self._price}"
      

# phone = Phone("nokia", 1100, 1000)
smartphone = Smartphone("oneplus", "5", 30000, "6 GB", "64 GB", "20 MP")
oneplus = FlagshipPhone("oneplus", "5t", 30000, "6 GB", "64 GB", "20 MP", "HybridSimSlot")
# print(phone.full_name())
# print(smartphone.full_name())
# print(smartphone2.full_name())
print(f"{oneplus.full_name()} and sim is {oneplus.hybridsim}")


# method resolution order (MRO)
# to see MRO
# print(help(FlagshipPhone))
# first is see called method in FlagshipPhone (current class) then its parent and then its parent class 
# print(oneplus.full_name()) 


# isinstance() 
# is used to check whether instance / object is given class or not
print(isinstance(oneplus, FlagshipPhone))
print(isinstance(oneplus, Smartphone)) # also true because oneplus is object of FlagshipPhone class which derived from Smartphone class
print(isinstance(smartphone, FlagshipPhone))

# issubclass()
print(issubclass(Smartphone, Phone)) # Smartphone class is sub part of Phone class // derived from Phone
print(issubclass(Phone, Smartphone))