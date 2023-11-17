# define a function take any no of lists containing number
# [1,2,3], [4,5,6], [7,8,9]
# return average
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3

# try to make this using lamba expression or anonymous function

# for two lists
def average_finder(l1,l2):
    average = []
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average

print(average_finder([1,2,3], [4,5,6]))

# for no of lists
def average_finder(*args):
    average = []
    for pair in zip(*args): # * is for unpacking the tuple to make list seperate and then zip ([],[])
        average.append(sum(pair)/len(pair))
    return average

print(average_finder([1,2,3], [4,5,6], [7,8,9]))

# using lambda expression
# lambda input/list as args form : output/return as list (so use list comp) 

average_lambda = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(average_lambda([1,2,3], [4,5,6], [7,8,9]))
