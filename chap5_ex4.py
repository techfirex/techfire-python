l = list(range(1,11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# main = []
odd = []
even = []

def odd_even(l):
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    
    output = [odd, even]
    return output 
            
    # main.append(odd)
    # main.append(even)
    # print(main)

print(odd_even(l))
