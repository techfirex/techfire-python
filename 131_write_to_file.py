# w r r+ mode

# w mode - write mode
# it overwrite the file content
# if file is not there then w mode create file
# when file is empty or you dont want to delete data which is already present in the file

# with open("filew.txt", "w") as f:
#     f.write("hello world")


# a mode - append mode
# it will append content to file in the end
# do not remove already written content from file
# this mode also can create file it there is no file present 

# with open("filea.txt", "a") as f:
#     f.write("this")


# r+ mode - write and read mode both 
# this start write from start cursor position and if there is some content in file then it will overwrite that portion using new content // for overcome this there solution in example using seek method
# this mode cannot create file because it also read file so it need file or file path to read and also have capability to write

with open("filea.txt", "r+") as f:
    f.seek(len(f.read()))
    f.write("this is r plus file")