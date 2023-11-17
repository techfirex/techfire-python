# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# third = int(input("Enter third number: "))

first, second, third = input("Enter three number with comma separated: ").split(",")

# average = (int(first) + int(second) + int(third))/3
# print("your average is {}".format(average))

# print(f"your average is {average}")


print(f"your average is {(int(first) + int(second) + int(third))/3}")