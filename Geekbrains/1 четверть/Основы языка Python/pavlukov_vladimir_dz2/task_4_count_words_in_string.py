"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове."""

# words = input()
words = 'hello world this is my life 1234567891113'


def count_words(string):
    separated_words = string.split(' ')
    for i, word in enumerate(separated_words):
        print(i, word[0:10])


count_words(words)
