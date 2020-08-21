# need to count the number of each vowel in the entered word

word = input("Provide a word to search for vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u']

found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:  # check ich letter in word
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, ' was found', v, 'time(s).')  # print all vowel in found
