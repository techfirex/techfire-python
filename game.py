import random

# win_number = randint(0, 101)
win_number = random.choice(range(0, 101, 2)) # for even number
# print(win_number)
guess_try = 1
game_over = False

guess_number = int(input("Enter number between 0 to 100: "))

while not game_over:
    if guess_number == win_number:
        print("YOU WON!")
        print(f"You guess in {guess_try} try") 
        guess_try += 1
        game_over = True
    else:
        if guess_number < win_number:
            print("too low")
            guess_try += 1
            guess_number = int(input("Enter number again: "))
        else:
            print("too high")
            guess_try += 1
            guess_number = int(input("Enter number again: "))