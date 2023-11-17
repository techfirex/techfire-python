# python debugger

import pdb # import pdb module

# module - python file which contains useful classes and functions wrote by developers

# According to wikipedia - Debugging is the process of finding and resolving defects or problems within a computer program that prevent  correct operation of computer software or a system.

# why debugging
# our program is not running and causing unexpected errors.
# our program is working fine but not working same way as we want.

# steps of debugging
# 1. set trace
# 2. execute code line by line

# example
pdb.set_trace() # in pdb l for see line and n for next line print and q for quite and c for continue code becasue after tracing error and solving it we want to run whole code
name = input("Enter your name: ")
age = input("Enter your age: ") 
# age = int(input("Enter your age: "))
print(f"your name is {name} and age is {age}")
age2 = age + 5
print(f"hello {name}, after 5 years your age will be {age2}")