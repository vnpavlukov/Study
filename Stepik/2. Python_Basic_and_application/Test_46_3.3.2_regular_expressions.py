import re  # regular expressions

'''
https://tproger.ru/translations/regular-expression-python/

re.match((pattern, string)  # подходит ли строка под шаблон
  re.match((pattern, string, re.IGNORECASE)  # игнорирование регистра
re.search  # находит первую подстроку которая подходит под шаблон
re.findall  # находит все подстроки которые подходят под шаблон
re.sub(old, new, text)  # заменят все вхождения подстрок под что-то другое

 . - Один любой символ, кроме новой строки \n
 ? - 0 или 1 вхождение шаблона слева. r"ab?c"  - abc или ac
 + - 1 и более вхождений шаблона слева 
        r"ab+c"  # любое число символов b не включая 0. abc, abbc
        r"a[ab]+a"  abaaba => ["abaaba"]
        * +  # метасимволы повтора являются жадными, т.е. находят макс длинну
        r"a[ab]+?c"  # убирает "жадность". abaaba => ["aba", "aba"]

\d - [0-9] -  \D - [^0-9]   цифры    исключаем цифры (всё кроме цифр)
\s - [\t\n\r\f\v] - пробельные символы
\S - [^\t\n\r\f\v] - исключаем пробельные символы
\w - [a-zA-Z0-9_] - буквы и цифры и _ 
\W - [^a-zA-Z0-9_] - исключающее буквы, цифры, _
\b - символ границы слова. Все слова с гласной буквы r'\b[aeiouAEIOU]\w+'
[..] - один из символов в скобках
[^..] — любой символ, кроме тех, что в скобках
^ и $	Начало и конец строки соответственно
. ^ $ " + ? {} [] \ | () - метасимволы (надо экранировать)
{n,m}	От n до m вхождений ({,m} — от 0 до m)
a|b	Соответствует a или b
()	Группирует выражение и возвращает найденный текст
    r'\@\w+.\w+'    abc.test@gmail.com      @gmail.com
    r'\@\w+.(\w+)'  abc.test@gmail.com      com

r"abc"  # значит что мы ищем именно abc
r"abc\?"  # ищем abc? (спец символы нужно экранировать)
r"a[abc]c"  # между а и с может быть любой из трех симв
r"a[a-d]c"  # диапазон символов от a до d
r"a[a-zA-Z]c"  # все большие а потом маленькие символы
r"a\wc"  # запись аналогичная выше
к"a[\w.]c" # как выше, но с точкой,найдет а.с
r"a[^a-zA-Z]c"  # ^ исключающий знак
r"ab*c"  # любое число символов b включая 0. abc, abbc, ac

r"ab{3}c"  # количество символов b. abbbc
r"ab{2-4}c"  # диапазон символов b.
r"test|text"  # поиск или. 
r"(text)"  # группировка символов

Полезные варианты:
r'\w+'  # разделим все слова по пробелу

'''

pattern = r"cat.*cat"  # значит что мы ищем именно abc
string = 'catabbacsfdgsfdgsdacat'
match_object = re.match(pattern, string)  # Nome
search_object = re.search(pattern, string)
# <re.Match object; span=(1, 4), match='abc'>
print('match:\t', match_object)
print('search:\t', search_object, '\n')

string = 'abc, acc, aac'
findall_object = re.findall(pattern, string)  # ['abc', 'acc', 'aac']
print('findall:', findall_object)

new_text = re.sub(pattern, 'abc', string)
print('sub:\t', new_text, '\n')


pattern = r"(test|text)"
string = 'texttext'
print('test:', re.search(pattern, string))
