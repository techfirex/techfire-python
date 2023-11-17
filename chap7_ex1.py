# exercise
# define function that takes number(n)
# return dictonary containing cube of number from 1 to n

# example
# cube_finder(3)
# {1:1, 2:8, 3:27}

def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes

print(cube_finder(3))
print(cube_finder(10))