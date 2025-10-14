"""
Word Occurrences
Estimate: 30mins
Actual:   27mins
"""

words_to_count = {}

words = input("Text: ").split()

for word in words:
    word = word.lower()
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1

sorted_words = sorted(words_to_count.keys())
max_word_length = max(len(word) for word in sorted_words)

for word in sorted_words:
    print(f"{word:{max_word_length}} : {words_to_count[word]}")
