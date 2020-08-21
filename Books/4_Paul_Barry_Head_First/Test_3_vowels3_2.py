# находит количество гласных в запрощенном слове и подсчитывает из количество

word = input("Provide a word to search for vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u']
found = {}  # пустой словарь
found = {'o': 0, 'u': 0, 'a': 0, 'i': 0, 'e': 0}    # зададим значения в пустом словаре

for letter in word:  # check ich letter in word
    if letter in vowels:
        found[letter] += 1

for n in found:
    print(n, ' was found', found[n],'time(s)' )  # print all vowel in found
