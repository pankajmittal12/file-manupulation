# Word Frequency Counter

filename = "sample.txt"

word_count = {}

with open(filename, "r") as file:
    text = file.read()

words = text.lower().split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Occurrences:")

for word in sorted(word_count):
    print(word, ":", word_count[word])