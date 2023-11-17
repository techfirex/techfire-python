# num to string
# define function

# example
input = [True, False, [1,2,3], 1, 1.0, 3]
# output = ["1","1.0","3"]

def num_to_string(l):
    output = [str(i) for i in input if (type(i) == float or type(i) == int)]
    print(output)

num_to_string(input)