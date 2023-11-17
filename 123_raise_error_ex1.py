# raise error example
# NotImplementedError
# abstract method - this concept is in java but in python we can do same using this error

class Animal:
    def __init__(self, name):
        self.name = name

    # def sound(self):
    #     return "this is animal sound"
    def sound(self): # this is abstact method like java 
        raise NotImplementedError("you have to define this method in subclass")
    # (abstact method means class function in which body we dont write anything or dont define anything)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self): # so here we define sound method for dog
        return "bhow bhow" 

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed 

    def sound(self): # so here we define sound method for cat
        return "meo meo"
    
doggy = Dog("boony", "pug")
print(doggy.sound())  # this will give sound of animal class so we have to give notimplementerror and tell that dont use sound method of animal class but implement each in its child class because all animals sound are different
