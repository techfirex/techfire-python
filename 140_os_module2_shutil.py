import os
import shutil

# os.walk() # it will walk around all files and folders # give generator iter object so we can loop over it

fileiter = os.walk(r"/home/tushar/Desktop/Coding Preparation")
print(fileiter)

# it will give three items
# for current_path, folder_names, file_names in fileiter:
#     print(f"current path : {current_path}")
#     print(f"folder names : {folder_names}")
#     print(f"file names : {file_names}")

# os.rmdir("folder_name") # remove dir if it is empty otherwise give error

os.makedirs("new/movies") # help to create folders inside folders
# create new folder and inside new creates movies folder


# shutil.rmtree("path_to_delete") # perminantly delete folder even if it is not empty

# shutil.copytree("new", "documents/new") # copy new folder to documents/new

# shutil.copytree("new", "documents/new123") # copy folder with changing name to new123

# shutil.copy("file.txt", "documents/file.txt") # copy file.txt to documents/file.txt 

# shutil.copy("file.txt", "documents/file123.txt") # copy file.txt with name change to document/flle123.txt

# shutil.move("file.txt", "documents/file.txt") # move files also you can change file name as earlier

# shutil.move("new", "movies/new") # also move folder and also you can change / rename folder name after moving