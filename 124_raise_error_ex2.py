# raise example 2

class Mobile:
    def __init__(self, name):
        self.name = name
    
class MobileStore:
    def __init__(self):
        self.mobiles = []
    
    def add_mobiles(self, new_mobile):
        # self.mobiles.append(new_mobile)
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("New mobile should be object of Mobile class")
    
oneplus = Mobile("one plus 6")
samsung = "samsung galaxy s8"

mobostore = MobileStore()

# mobostore.add_mobiles(samsung) 
mobostore.add_mobiles(oneplus)

print(mobostore.mobiles)

mobo_phones = mobostore.mobiles
print(mobo_phones[0].name)

