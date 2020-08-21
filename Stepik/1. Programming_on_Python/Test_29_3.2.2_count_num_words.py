words_1 = [n.lower() for n in input().split(' ')]


def count_num_words(words):
    d = dict()
    for i in words:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


for key, values in count_num_words(words_1).items():
    print(key, values)
