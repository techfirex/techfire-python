# reading files having emoji
# UnicodeDecodeError - sometimes emoji character not read by machine and give error
    
# with open("small_love_story.txt", "r", encoding="utf-8") as rf:
#     print(rf.encoding)
#     data = rf.read()
#     print(data)

# reading long files in chunk - for memory efficient
with open("love_story.txt","r") as rf:
    data = rf.read(100) 
    while (len(data) > 0):
        print(data)
        data = rf.read(100)


