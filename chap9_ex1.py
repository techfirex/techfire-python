# define function that takes list of strings
# list containing reverse of every strings
# use list comprehension

# example
l = ["abc","tuv","xyz"]
# reverse_string(l) >>> ["cba","vut","zyx"]

def reverse_string(l):
    reverse = []
    for i in l:
        reverse.append(i[::-1])
    print(reverse)

reverse_string(l)



def reverse_string_lc(l):
    revered = [i[::-1] for i in l]

reverse_string(l)

