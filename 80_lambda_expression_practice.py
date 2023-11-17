def is_even(a):
    if a%2 == 0:
        return True
    else: 
        return False

print(is_even(5))


def is_even(a):
    return a%2 == 0

print(is_even(5))


is_even2 = lambda a : a%2  == 0
print(is_even2(6))




def last_char(s):
    return s[-1]
print(last_char("tushar"))

last_char2 = lambda s : s[-1]
print(last_char2("makwana"))


# lambda with if and else
def func(s):
    if len(s) > 5:
        return True
    else: 
        return False
print(func("abc"))
print(func("abcdef"))


def func(s):
    if len(s) > 5:
        return True
    return False # without else
print(func("abc"))
print(func("abcdef"))


def func(s):
    return len(s) > 5 # without if else

print(func("abc"))
print(func("abcdef"))


func2 = lambda s : True if len(s) > 5 else False
print(func2("Tushar"))

func2 = lambda s : len(s) > 5
print(func2("Tus"))