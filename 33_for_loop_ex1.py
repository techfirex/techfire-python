# 1   2   5   6
# 0   1   2   3

num = input("Enter number: ")
sum = 0
for i in range(0, len(num)):
    sum += int(num[i])
print(sum)