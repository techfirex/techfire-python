squares = {num:num*2 for num in range(1,11)}
print(squares)

squares_next = {f"squares of {num} is":num*2 for num in range(1,11)}
for k,v in squares_next.items():
    print(f"{k}: {v}")

# word count
string = "tuuusharrr"
word_count = {char:string.count(char) for char in string}
print(word_count)