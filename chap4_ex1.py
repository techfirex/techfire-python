# two parameter
# def greater_of_two(num1, num2):
#     if num1>num2:
#         return num1 
#     return num2 # else can be used but ommited
# print(greater_of_two(4,5)) # take is from user using input
# print(greater_of_two(50,5)) 

# three parameter
def greatest(a,b,c):
    if a > b and a > c:
        return f"{a} is greatest"
    elif b > a and b > c:
        return f"{b} is greatest"
    else:
        return f"{c} is greatest"
print(greatest(5,6,7))
print(greatest(67,100,45))