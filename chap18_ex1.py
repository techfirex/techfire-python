# input file1.txt
# Tushar, 50
# Chaitanya, 100
# Milind, 200

# output file2.txt
# Tushar's salary is 50 
# chaitanya's salary is 100 
# Milind's salary is 200 

with open("file1.txt", "r") as rf:
    with open("file2.txt", "a") as wf:
        for line in rf.readlines():
            name, salary = line.split(",")
            wf.write(f"{name}'s salary is {salary}")