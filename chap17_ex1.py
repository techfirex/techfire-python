# divide function 
# exception handling
# ZeroDivisionError

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Please don't divide by zero"
    # except ZeroDivisionError as error: # default msg store in error 
    #     return error
    except TypeError:
        return "Please input numbers only"
    except:
        return "unexpected error"

print(divide(4,2))
print(divide(4,0))
print(divide('4',1))
print(divide(4,'3'))
print(divide('8','7'))