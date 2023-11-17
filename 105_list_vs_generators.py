# list vs generators
# memory usage
# time
# when to use list
# when to use generator


import time

t1 = time.time()
l = [i**2 for i in range(1000000)]
t2 = time.time()
print(t2-t1)

t1 = time.time()
g = (i**2 for i in range(1000000))
t2 = time.time()
print(t2-t1)