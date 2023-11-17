# data stracture
# list - ordered collection of items
# you can store anything in list like interger, float, string, etc

numbers = [1,2,3,4,5]
print(numbers)
print(numbers[3]) # same as string slicing # accessing items from list

words = ["word1","word2","word3","word4",]
print(words)
print(words[:2])

mixed = [1,2,3,"four","five",6.5,7,None]
print(mixed)
print(mixed[-1])

mixed[1] = "two"
print(mixed)

mixed[1:] = "three"
print(mixed)

mixed[1:] = ["two","three","four"]
print(mixed)

