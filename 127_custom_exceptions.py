# Python custom exceptions
# Why custom exceptions?
# To increase readability of code

# example
class NameTooShortError(ValueError):
    pass


def validate(name):
        if len(name) < 8:
            raise NameTooShortError("name is too short")

username = input("Enter you name: ")
validate(username)
print(f" hello {username}")