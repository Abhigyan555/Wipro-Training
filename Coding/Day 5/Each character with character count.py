text = "Python is fun"
text = text.replace(" ", "")  # remove spaces

char_count = {}

for char in text:
    char_count.setdefault(char, 0)
    char_count[char] += 1

for char in char_count:
    print(char, ":", char_count[char])
