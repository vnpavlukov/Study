# https://stepik.org/lesson/24470/step/11?unit=6776
import re

text = ['this is a.text this.cool',
        'Two*****words']

pattern_first_letter = r'\b\w'
pattern_second_letter = r'\b\w(\w)'

for line in text:
    new_line = ''
    words = re.split(r'\b', line)

    for word in words:
        if re.findall(pattern_second_letter, word):
            first_letter = re.findall(pattern_first_letter, word)
            second_letter = re.findall(pattern_second_letter, word)
            word = re.sub(second_letter[0], first_letter[0], word, 1)
            word = re.sub(first_letter[0], second_letter[0], word, 1)
        new_line += word
    print(new_line.rstrip())

