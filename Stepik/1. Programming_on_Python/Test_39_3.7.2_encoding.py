key = input()
value = input()
encoding = input()
decoding = input()

dictionary = {}
n = 0

for letter in key:
    dictionary[letter] = value[n]
    n += 1

for keys in encoding:
    print(dictionary[keys], end='')
print()

for i in range(0, len(decoding)):
    for keys, values in dictionary.items():
        if decoding[i] == values:
            print(keys, end='')
