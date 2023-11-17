# fibonacci series
# 0 1 1 2 3 5 8 13 21 34

# n = 1 --> 0
# n = 2 --> 1
# n = 3 --> 0+1 = 1
# n = 4 --> 1+1 = 2
# n = 5 --> 1+2 = 3

def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b,end= " ")
    else:
        print(a,b,end= " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b,end=" ")

fibonacci(10)
# print(fibonacci(10))

# 0 1 1 2 3 5 8 13 21 34