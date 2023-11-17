# functions
# buit in functions - len()

# parameters - function input during creating, ex num1 & num2
# arguements - function input during calling, ex a & b or first_name & last_name

def add_two(num1, num2):
    return num1 + num2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(add_two(a,b))

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(add_two(first_name,last_name))
