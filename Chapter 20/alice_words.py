import string

file = open("alice_in_wonderland.txt", 'r')
book_words = file.read()
file.close()

book_words = book_words.lower()
book_words = book_words.split()

formatted_words = []
for word in book_words:
    formatted_word = ""
    for char in word:
        if not (char in string.punctuation or char in string.digits):
            formatted_word += char
    if formatted_word != "":
        formatted_words.append(formatted_word)

formatted_words.sort()

freq_table = {}
for word in formatted_words:
    freq_table[word] = freq_table.get(word, 0) + 1

output = open("output.txt", "w")
len_long_word = 0

for word in freq_table:
    if len(word) > len_long_word:
        len_long_word = len(word)

lines = []
row_len = len("Word" + (" " * (len_long_word+1 - 4)) + "Count\n")
lines.append("Word" + (" " * (len_long_word+1 - 4)) + "Count\n")
lines.append("=" * row_len + "\n")

for word in freq_table:
    lines.append(word + (" " * (len_long_word+1 - len(word))) + str(freq_table[word]) + "\n")

output.writelines(lines)

output.close()

