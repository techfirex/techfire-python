# define generator function
# take one number as argument
# generate sequence of even numbers from 1 to that number
# example
# input 5 > 2,4
# input 7 > 2,4,6

def even_generator(n):
    for i in range(1,n+1):
        if i%2 == 0:
            yield i 

print(even_generator(10))
for i in even_generator(5):
    print(i)
