names = ["tushar", "milind", "chaitanya"]

def func(l, **kwargs):
    if kwargs.get("reverse_str"): # beacuse it is dict
        return [i[::-1].capitalize() for i in names] # .title() method also work
    else:
        return [i.capitalize() for i in names]

print(func(names))
print(func(names, reverse_str = True))
