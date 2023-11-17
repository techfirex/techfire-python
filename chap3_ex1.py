# number guessing game
from random import randint

winning_number = randint(0,100)
guessing_number = int(input("Enter number: "))

if winning_number == guessing_number:
    print("You Won!")
elif winning_number > guessing_number:
    print("low")
else:
    print("high")
    
print(winning_number)
    