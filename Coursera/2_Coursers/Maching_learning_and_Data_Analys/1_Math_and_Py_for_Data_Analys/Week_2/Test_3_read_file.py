import numpy as np

all_words = dict()

with open('sentences.txt') as file:
    for line in file:
        for word in line.split():
            clean_word = word.strip('.,!').lower()
            if clean_word not in all_words:
                all_words[clean_word] = 0
            all_words[clean_word] += 1

print(all_words)