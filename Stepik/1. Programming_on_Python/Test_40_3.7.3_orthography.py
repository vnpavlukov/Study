input_count = int(input())
dictionary = []

for i in range(input_count):
    dictionary.append(input())

input_count = int(input())
text = []
for input_text in range(input_count):
    for word in input().split():
        text.append(word)


def find_difference(list_1, list_2):
    low_list_1 = [x.lower() for x in list_1]
    n = 0
    unique = []
    for word in list_2:
        if word.lower() not in low_list_1:
            unique.append(list_2[n])
        n += 1
    return unique


dif = set(find_difference(dictionary, text))

for i in dif:
    print(i)
