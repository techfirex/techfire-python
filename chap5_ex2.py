numbers = [1,2,3,4]
words = ["word1", "word2", "word3", "word4"]

# using append and pop method
reverse_numbers = []
for i in range(len(numbers)):
    reverse_numbers.append(numbers.pop())
print(reverse_numbers)

reverse_words = []
for i in range(len(words)):
    reverse_words.append(words.pop())
print(reverse_words)

# function making
def return_list(l):
    reverse_numbers = []
    for i in range(len(numbers)):
        reverse_numbers.append(numbers.pop())
    print(reverse_numbers)
    
    
# using reverse method
def reverse_list(l):
    l.reverse() # return l.reverse() --> this will give None // direct return doesn't work bcz it will change the list and give return final changed list
    return l
numbers = [1,2,3,4]
print(reverse_list(numbers))

# using list slicing // same as string slicing
def reverse_words(l):
    return l[::-1]
words = ["word1", "word2", "word3", "word4"]
print(reverse_words(words))

