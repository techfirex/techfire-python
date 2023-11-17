class A:
    def class_a_method(self):
        return "this is class A method"
    
    def hello(self):
        return "hello from class A"


class B:
    def class_b_method(self):
        return "this is class B method"
    
    def hello(self):
        return "hello from class B"
    
instance_a = A()
instance_b = B()

print(instance_a.class_a_method())
print(instance_b.class_b_method())


class C(A,B): # multiple inheritance // class C derived from A and B
    pass
    # when call hello() it in both A and B which is called first is based on MRO
    # in this case MRO is C,A,B // [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
    # if we create // class C(B,A) then it is C,B,A

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())


# check of MRO three methods
# print(help(C)) # give full readable details
print(C.mro()) # print in list form
print(C.__mro__) # print in tuple form
