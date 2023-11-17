# else and finally clause in Exception handling

while True:
    try:
        number = int(input("Enter your age: "))
    except ValueError:
        print("you entered string instead of numbers and try again ...")
    except:
        print("unexpected error")
    else: # when try block run successful then else also run
        print(f"user inpur = {number}")
        break
    finally: # always run
        print("finally block")