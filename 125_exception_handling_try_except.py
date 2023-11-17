# exception handling
# try except else finally

# exception is errors which occurs at execution time
# to solve/handle we use try except 

while True:
    try:
        age = int(input("Enter your age: ")) # here user can enter string instead of integer then error
        break
    except ValueError:
        print("you entered string instead of numbers and try again ...")
    except:
        print("unexpected error")
    

if age < 18:
    print("you can't play this game")
else:
    print("you can play this game")