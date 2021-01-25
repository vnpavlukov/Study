"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу
должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать
написанную ранее функцию int_func()."""

new_word = 'letter'


def int_func(word):
    return chr(ord(word[0]) - 32) + word[1:]


print(int_func(new_word))


def title_register(sentence):
    words = sentence.split()
    words_list = list()
    for word in words:
        words_list.append(int_func(word))
    return ' '.join(words_list)


example = 'mom was washing the frame!'
print(title_register(example))
