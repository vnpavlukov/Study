"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

in_filename = 'task_4_in.txt'
out_filename = 'task_4_out.txt'

translation_words = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
    'zero': 'ноль',
}

with open(in_filename, 'r', encoding='utf-8') as f_in:
    with open(out_filename, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            words_in_line = line.lower().split()
            new_line = list()
            for word in words_in_line:
                if word in translation_words:
                    new_line.append(translation_words[word])
                else:
                    new_line.append(word)
            f_out.write(' '.join(new_line) + '\n')
