# находит количество гласных в запрощенном слове

word = input("Provide a word to search for vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u']
found = []  # пустой список
for letter in word:  # check ich letter in word
    if letter in vowels:
        if letter not in found:
            found.append(letter)  # add new letter in list found if this letter not in this list

for vowel in found:
    print(vowel)
