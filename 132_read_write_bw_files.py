# copy content from file1 to file2

with open("file1.txt", "r") as rf:
    with open("file2.txt", "w") as wf:
        wf.write(rf.read())