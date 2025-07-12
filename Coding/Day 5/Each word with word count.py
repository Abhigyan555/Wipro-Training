text = "Python is easy and Python is powerful"

words = text.split()
word_count = {}

for word in words:
    word_count.setdefault(word, 0)
    word_count[word] += 1

for word in word_count:
    print(word, ":", word_count[word])
